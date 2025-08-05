# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30f647c5-48a4-3467-807e-576e3a473985 | -10.468 | -44.376301 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fff76f56-2a0b-340e-b18f-d1264f8f3e07 | -18.861099 | -40.455799 | 2025-08-05 00:28:00 | METOP-C | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed217b6b-5afb-3286-ba72-b2f614b65c9b | -8.2617 | -45.056999 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7e264b27-3dbe-341f-8c02-4cb9150ffcb5 | -10.3332 | -47.8176 | 2025-08-05 00:28:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d95fc095-5929-3948-8670-63fc42c6dc06 | -10.3493 | -44.901501 | 2025-08-05 00:28:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 113554c6-1d3e-3bb0-bd57-07e9c76778f6 | -14.4943 | -52.090199 | 2025-08-05 00:28:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 28f80c41-8c5c-3571-9b6d-e82dc62d7c44 | -10.4876 | -44.371799 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c8b7dba5-a7e8-326b-accb-5bb665797ea5 | -12.5224 | -47.177799 | 2025-08-05 00:28:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6cca536-44b1-3fd8-b516-685335e3a689 | -8.242 | -45.061401 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 45f7c00c-1746-3e1f-923e-96b2a9e1a1bc | -8.2503 | -45.052299 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba9ee5c9-c589-325d-8ac9-13d2536f6833 | -4.7877 | -45.332901 | 2025-08-05 00:28:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf645a8f-d65c-30b2-9574-07fd7aa9b7e8 | -9.0659 | -45.0583 | 2025-08-05 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cdda8ca-7b8e-31d7-ba91-21c46a4a4990 | -8.015 | -43.126701 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 840ad85f-712c-3480-8e2a-2a5028851c75 | -6.4559 | -44.555 | 2025-08-05 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca7f3ec-91ec-39ff-9f8a-e104a3e2bb79 | -3.4818 | -43.250702 | 2025-08-05 00:28:00 | METOP-C | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f6624e1-34a4-317e-a454-3916cfd53006 | -8.0088 | -43.233398 | 2025-08-05 00:28:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5901440-5e81-31a1-835b-1a2246a44e73 | -5.146 | -36.369801 | 2025-08-05 00:28:00 | METOP-C | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 330d9f47-967f-3b20-a0c8-9aeac3785091 | -7.9068 | -45.538101 | 2025-08-05 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3bc3ba1-786f-337e-aef5-e1b526b2b094 | -8.0813 | -42.967499 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 428b2433-5afe-32c5-b341-c4c32c3bf437 | -12.7342 | -46.394501 | 2025-08-05 00:28:00 | METOP-C | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac72432-bb76-339f-8ee9-ff94a344a93a | -9.4052 | -45.513901 | 2025-08-05 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54d60161-b95f-3ceb-b759-5c2d89b95319 | -12.7123 | -48.0784 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc045a86-5e77-3b03-a93e-d3b05d6399a6 | -10.3352 | -47.826599 | 2025-08-05 00:28:00 | METOP-C | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b1e7d51-cfdf-3b76-a2b7-cb280218532e | -7.3503 | -44.677101 | 2025-08-05 00:28:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f46c5c4-839f-3156-9e70-7d0643e78561 | -9.0674 | -45.0653 | 2025-08-05 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 628d867f-8064-314a-b0d1-c9ffae3ad7b9 | -11.2794 | -44.639702 | 2025-08-05 00:28:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bdab0650-1155-3b2e-a243-7de5ff1efb80 | -10.4844 | -44.358002 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95b0d77c-857d-3b82-a600-789a8ebfe4f7 | -8.0085 | -43.143299 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e798da8-5a09-3cbd-a05c-30be2066eb33 | -6.712 | -44.098301 | 2025-08-05 00:28:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1ea58a03-d120-345f-a695-94bc868f059b | -6.9744 | -42.869202 | 2025-08-05 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f003cc6b-48c0-3804-896c-c07c9d04a49e | -6.6846 | -49.798 | 2025-08-05 00:28:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b218f3d-e79c-386f-aad6-b6a0577dd207 | -8.2518 | -45.0592 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 13676a21-2aa0-3bc4-9235-a78ba6839bd2 | -5.8227 | -46.9841 | 2025-08-05 00:28:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 222846a2-96f2-38de-9b57-064f1917d26c | -8.0166 | -43.133801 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aee03324-8985-328f-8998-17a3c8ee5e6c | -11.8223 | -44.258499 | 2025-08-05 00:28:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2f729f8-cd75-3fa8-91db-b9cee5eaa4d7 | -6.7104 | -44.0914 | 2025-08-05 00:28:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 167c24bd-fe58-3a56-ac45-a4a004706176 | -7.4045 | -44.643299 | 2025-08-05 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 57a47fa1-b0c4-3256-9a10-a786ccb3d7dc | -8.0249 | -43.169601 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06bd66f5-a1dd-33f2-a95c-e6c54e2a9e3c | -12.5243 | -47.186699 | 2025-08-05 00:28:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97b91011-13ff-362a-bec0-1f79b8f97b0d | -7.9922 | -43.162102 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea451cb6-7728-3f99-844e-efb5cf9e49b6 | -11.8207 | -44.251499 | 2025-08-05 00:28:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a7a881d6-5ad5-30e3-9e97-e8ec5d049850 | -8.002 | -43.159801 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c410988d-9f26-3083-bb1a-da31d179f363 | -4.7795 | -45.3419 | 2025-08-05 00:28:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7ae0485-a7ae-39e3-9cfc-54ad0bc68c42 | -10.4778 | -44.3741 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b49426b9-03c2-3bf7-9687-4e235459e8ec | -4.7763 | -45.328201 | 2025-08-05 00:28:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0d57d6f-8b83-3969-95b2-8fae4b223850 | -7.7217 | -43.9123 | 2025-08-05 00:28:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2122b17e-286f-31a9-895d-503b0bd0e1cf | -6.385 | -43.709702 | 2025-08-05 00:28:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a6105ce-8993-35a4-8649-fc2a1cf2a460 | -4.7779 | -45.335098 | 2025-08-05 00:28:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6296f0c4-4c4b-3ce2-95bb-f5b213043f21 | -15.6956 | -48.969398 | 2025-08-05 00:28:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6e12ce49-9a82-38be-99e9-cbf9885547de | -11.8239 | -44.265499 | 2025-08-05 00:28:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 938ae670-a351-312a-94ac-edab69d91bf9 | -12.3636 | -46.057301 | 2025-08-05 00:28:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7895f758-038a-31a0-a430-60e8d0f3c30d | -10.4793 | -44.381001 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ea371a1e-d998-3a5d-a4e1-8e3754efc936 | -6.6823 | -49.787701 | 2025-08-05 00:28:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f913130-1413-3e82-b2df-36e9043766c8 | -11.0466 | -47.6077 | 2025-08-05 00:28:00 | METOP-C | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7accae6-eadd-3a8f-b325-a4bcb9de948d | -5.6116 | -45.327499 | 2025-08-05 00:28:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cc839c0-11fc-3a02-9a98-34d0e110aa83 | -8.9452 | -46.728802 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 103fd1f9-223a-3c05-b482-22e5002c3a61 | -8.7226 | -46.421001 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b7288b8-68cf-3ee7-9413-0dad912c8ef7 | -7.4013 | -44.629601 | 2025-08-05 00:28:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| caf4fbd4-6e0d-34d0-9bdd-dad08ef911f9 | -10.5344 | -42.5494 | 2025-08-05 00:28:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 485398ea-cb7b-3858-a721-66dc85da7357 | -8.0169 | -43.223999 | 2025-08-05 00:28:00 | METOP-C | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eba32b91-13d2-339b-9ab5-c75eeea6444f | -7.1257 | -47.841801 | 2025-08-05 00:28:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 33de6256-c9e3-319e-ad18-b511ba234649 | -12.7144 | -48.088402 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e392a21d-b2d9-3e8d-9f2c-9575056d741d | -7.9166 | -45.5359 | 2025-08-05 00:28:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a427959-1dab-3dc1-a652-99fcf1cce12e | -8.2389 | -45.0476 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aaa41a48-5bab-3afd-a9bc-6e8f88cd117b | -9.402 | -45.499699 | 2025-08-05 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27b2d8f5-19cc-3f41-bf9b-edbbff7c6dcb | -7.8668 | -46.735401 | 2025-08-05 00:28:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 222f4e94-4a8c-3511-bf1e-60a246000a1c | -8.7455 | -46.431499 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a16e02ef-317c-39c5-8dfe-1eff462465d1 | -5.6569 | -42.576302 | 2025-08-05 00:28:00 | METOP-C | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 195592f0-900b-3f20-a5dd-17da3b5688f8 | -15.7054 | -48.9674 | 2025-08-05 00:28:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f047012-10d2-3b0e-bcaa-6ad767491aae | -8.955 | -46.726601 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22a2c7a0-f6a3-3955-aa1d-f0ee0d7cba15 | -8.9567 | -46.734299 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e77206b-51dc-35c3-9c1a-6f44d78669da | -6.9709 | -42.8545 | 2025-08-05 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a26d1392-cd35-3af9-8c8c-0c9594540208 | -10.9316 | -48.363998 | 2025-08-05 00:28:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c6d995d-f481-3b6f-b539-dc9d1e2cdf66 | -9.1752 | -40.594898 | 2025-08-05 00:28:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 408db3b3-a450-3ee5-bda4-c241ad525c38 | -14.3596 | -47.104401 | 2025-08-05 00:28:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 888b2590-2fb3-33fc-8cbd-480265c5edda | -11.7517 | -45.002899 | 2025-08-05 00:28:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 762f7d6d-e661-37d1-9263-e3449984fa2d | -5.4865 | -42.157001 | 2025-08-05 00:28:00 | METOP-C | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ab1c9fe-8e49-35b5-ab68-92784d64401a | -6.4688 | -44.566502 | 2025-08-05 00:28:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ca4bbdd-2d29-35e0-a1f4-5076f90b7092 | -8.9585 | -46.742001 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 32a1ad7c-a09d-3a5a-9590-1b5a6c6bd3d7 | -8.2291 | -45.049801 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9406f9fc-e6b8-3fd3-ab0b-78fc779280e7 | -6.9062 | -52.8559 | 2025-08-05 00:28:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2232ca63-0ce3-3821-ad6c-a249d86f26aa | -7.9906 | -43.1549 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8bc397a6-8719-385b-bc9f-7109d66de498 | -9.0561 | -45.060501 | 2025-08-05 00:28:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6fe3d5a6-b975-35da-bb26-bc4bc73cee86 | -4.7861 | -45.326 | 2025-08-05 00:28:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0f355ee-a9a7-3631-b5b0-519300f368c4 | -12.7242 | -48.0863 | 2025-08-05 00:28:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d604fc50-3ea8-3a89-b8fb-421c73792a06 | -8.2746 | -45.0686 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b2b63f6-32b8-33dc-9843-fcf3829546eb | -10.5808 | -50.4865 | 2025-08-05 00:28:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b6a081e-bfda-3905-b3c6-541c78f04afb | -18.862801 | -40.463402 | 2025-08-05 00:28:00 | METOP-C | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e82ebbd4-cdf0-3679-b428-73ad26b2c366 | -8.2648 | -45.070801 | 2025-08-05 00:28:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8c37ed08-7d27-37b4-a92f-f3885b2bef49 | -15.698 | -48.981998 | 2025-08-05 00:28:00 | METOP-C | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5a6899b0-e88e-3db6-a8c1-953f1e45de4c | -6.9825 | -42.8596 | 2025-08-05 00:28:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1be0a452-9588-37c0-b592-6f64db15127e | -9.4102 | -45.490398 | 2025-08-05 00:28:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17b73e34-7629-3e89-88ea-9235d1765a4d | -6.3882 | -43.723701 | 2025-08-05 00:28:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df1e86b5-50af-33e2-a4b9-78f214276434 | -10.4499 | -44.387699 | 2025-08-05 00:28:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1ca40a-2698-3438-8c8e-e84b622c8894 | -8.0264 | -43.131599 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e65dc02-b657-3f9f-bd42-f765a6fe4d54 | -8.9665 | -46.732201 | 2025-08-05 00:28:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3c204f8-c03c-372f-879c-d4ccf32ea764 | -9.5633 | -40.360199 | 2025-08-05 00:28:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 999fa69e-f4c7-3cfe-8461-a5a6d4420715 | -8.0183 | -43.140999 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 342bc77b-8dda-368c-b758-d1374e3290ad | -10.9218 | -48.3661 | 2025-08-05 00:28:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f84a9ba-b231-36ca-957e-a79149608bbc | -8.0829 | -42.974701 | 2025-08-05 00:28:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README3.md)
