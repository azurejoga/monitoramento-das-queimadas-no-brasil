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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02d249e6-bb52-3454-a522-fd08f90d5735 | -5.8265 | -43.5872 | 2026-07-15 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 4894d07e-0c7c-3a4a-a1e6-06b7be2c8868 | -12.3561 | -47.413 | 2026-07-15 00:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| c821bb36-d8a5-3c22-9da9-cad4dc9a2b0e | -9.7474 | -49.0465 | 2026-07-15 00:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 2dadda3c-d5e2-3cd5-800c-742d50f752e0 | -9.7285 | -49.0484 | 2026-07-15 00:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| d7496378-0376-3234-be92-4a7819675323 | -12.3561 | -47.413 | 2026-07-15 00:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e52826b6-7f76-335b-97a8-381227ab861c | -9.7285 | -49.0484 | 2026-07-15 00:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ca834056-54d1-34b0-97a3-91899eddec1d | -5.8265 | -43.5872 | 2026-07-15 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f825c150-09b5-3534-986c-acf5e49eb91c | -9.7474 | -49.0465 | 2026-07-15 00:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 7417c07f-ab7d-3dab-b426-151770e55ba7 | -9.7477 | -49.0248 | 2026-07-15 00:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0a3ede5b-21f6-3413-8ad0-4b3596f90f85 | -23.7959 | -48.45433 | 2026-07-15 00:16:00 | TERRA_M-M | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| b85af0f6-3e86-3b56-ba49-dfc9d3c069e4 | -21.24519 | -49.03694 | 2026-07-15 00:16:00 | TERRA_M-M | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 33293eb0-cf0f-39bd-8e54-32c5c3a42544 | -22.1008 | -46.99408 | 2026-07-15 00:16:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 241388cd-90c5-351f-8f0f-3fdc513c8e86 | -22.37795 | -49.79124 | 2026-07-15 00:16:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 54c43641-d898-3f3f-8e13-c09e7dec2cf2 | -22.10238 | -47.00457 | 2026-07-15 00:16:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0cc96051-bcbb-3687-9adf-d418aa43f776 | -21.83358 | -50.76382 | 2026-07-15 00:16:00 | TERRA_M-M | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| c69c4838-9096-3384-8ba1-37571d539cce | -21.47847 | -47.33828 | 2026-07-15 00:16:00 | TERRA_M-M | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cf93ac5f-f0ab-3219-aa9e-6e7986cad51b | -20.6508 | -48.67591 | 2026-07-15 00:16:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d39d99f7-a56e-3c4e-9201-cdbc1703ef51 | -20.65216 | -48.68544 | 2026-07-15 00:16:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e063aeda-eac3-3a06-831a-2ab85e598b1f | -12.45239 | -49.59417 | 2026-07-15 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 622cdb69-33a3-3290-a711-00036e857350 | -14.21081 | -47.40693 | 2026-07-15 00:18:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 32f70764-d9af-3ec6-9216-5347ec320546 | -16.39791 | -49.93156 | 2026-07-15 00:18:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 95a48160-92ce-3001-ad30-7ed24c3e7d02 | -13.43977 | -43.85629 | 2026-07-15 00:18:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 12d0bb31-3e78-37ea-ae2e-cf82d152322e | -14.82925 | -44.21126 | 2026-07-15 00:18:00 | TERRA_M-M | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 99cc3558-3cb0-3634-9d17-51ccc2769a45 | -12.44188 | -49.58589 | 2026-07-15 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c4aa3c2a-0fd1-3123-a1e1-ed67a4480f99 | -18.78532 | -52.4139 | 2026-07-15 00:18:00 | TERRA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5beab990-ea25-3e9a-9dba-ababc4f91c6a | -12.35688 | -47.41346 | 2026-07-15 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| a8bc26c6-0718-3d66-803e-be1fccb654c2 | -18.78397 | -52.40305 | 2026-07-15 00:18:00 | TERRA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0d2ad844-91e5-3b39-a9aa-8181ebb1775f | -18.49513 | -46.94161 | 2026-07-15 00:18:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 23959630-da98-374c-b19c-a368fa888b8d | -16.71086 | -49.34603 | 2026-07-15 00:18:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d24bf2ed-e3ac-3019-9081-7b2805c57fbd | -14.21264 | -47.41891 | 2026-07-15 00:18:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 36f02ab6-8512-33e6-a07e-66caf5fe0837 | -13.43591 | -43.83369 | 2026-07-15 00:18:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4c77cd25-8b37-3e26-82fb-a047eb0c10cb | -16.70952 | -49.33664 | 2026-07-15 00:18:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fb224324-d768-3afe-86e4-ff4d6efacd38 | -16.38906 | -49.93293 | 2026-07-15 00:18:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 95b38e9e-e744-31f8-8161-55c63421de42 | -12.35882 | -47.42609 | 2026-07-15 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8c0caff3-df6b-30bc-b323-9186ec377a4f | -12.66643 | -48.23568 | 2026-07-15 00:18:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1961b066-3dde-3ace-af41-e02443af38fd | -12.65667 | -48.23723 | 2026-07-15 00:18:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 41a710e2-4471-3f19-9f8d-ab74fa268f1d | -12.45102 | -49.58453 | 2026-07-15 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 96b498d8-b76d-3e1d-91e3-6ead0008ef1e | -9.7474 | -49.0465 | 2026-07-15 00:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 9f71fc39-de09-3725-9852-f14fb5d3fe39 | -12.3561 | -47.413 | 2026-07-15 00:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| d5f89f51-2d93-3e2e-9f10-6173bb796216 | -9.7285 | -49.0484 | 2026-07-15 00:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b887f179-3de6-370b-ad2d-76f2b3a577dc | -5.8265 | -43.5872 | 2026-07-15 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7d2a660b-ed02-382d-b003-2bee370446be | -12.86908 | -58.27608 | 2026-07-15 00:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1e116720-5205-3740-b24a-edf69eb9b406 | -9.88141 | -49.98628 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 9ddf2e8e-9897-31ab-b7a8-b88aecfacc7c | -12.53778 | -57.21341 | 2026-07-15 00:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f8739ea0-6142-3818-bfe9-311d9f078979 | -8.74615 | -49.448 | 2026-07-15 00:20:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f99d4a75-1b32-3206-991f-79344e9e31f8 | -3.15864 | -48.57478 | 2026-07-15 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 773ec45d-6ad0-324a-b639-e85541745bf8 | -9.18869 | -50.88294 | 2026-07-15 00:20:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0b367c8d-7b74-3814-ab2c-0d68ee6bb514 | -8.95078 | -47.60974 | 2026-07-15 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a8816e97-a378-3d51-852f-782ff33f69b3 | -2.79141 | -49.52372 | 2026-07-15 00:20:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c69ac9d7-013c-3a20-8ec5-82e3572a3045 | -9.1874 | -50.8738 | 2026-07-15 00:20:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8723e774-73b2-3206-9b38-f785d697dfcb | -8.94478 | -47.61825 | 2026-07-15 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| fe048aed-b41c-33d2-98f4-722c70100aa5 | -8.45297 | -51.5512 | 2026-07-15 00:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33ddaff8-3eb4-3685-9e40-adc7183e9b1e | -5.83609 | -43.59246 | 2026-07-15 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 4306f0a0-17dc-3e09-a98c-696f0bf339ea | -12.88261 | -58.27438 | 2026-07-15 00:20:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 853c1661-41e1-34dd-a167-37254319659f | -10.45519 | -55.06799 | 2026-07-15 00:20:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3bfac6e9-dbfa-3011-a20b-751d2e0f6907 | -5.35342 | -45.19955 | 2026-07-15 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 18cb1df5-fb77-321d-9b16-c6b12f10dbaf | -9.51529 | -47.14548 | 2026-07-15 00:20:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7d32fb53-037b-3288-aad0-e472976e9b6b | -2.7671 | -48.56794 | 2026-07-15 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b92b1f06-c0ab-355f-aa12-c156172e42c5 | -6.67259 | -47.52098 | 2026-07-15 00:20:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bbc0e2fb-3595-3bf8-9301-0b7f0c539187 | -11.0944 | -47.80476 | 2026-07-15 00:20:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 68d5828c-a7b1-38bc-9f6d-5423c75cc109 | -9.88001 | -49.97659 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8ad84980-f439-3dc0-802b-6967021aa8d7 | -12.54071 | -57.2075 | 2026-07-15 00:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8feb04fd-f217-3ba2-9493-ee588ec9dd71 | -3.21773 | -49.48808 | 2026-07-15 00:20:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1d1687f9-fc30-37c7-af8f-3694bb58e797 | -10.50861 | -50.05605 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 994a0611-479f-3f22-b54a-89aad45e2c79 | -9.6578 | -48.10919 | 2026-07-15 00:20:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 910a5c72-16bb-33fb-9804-20fdf73ee21f | -5.82036 | -43.59491 | 2026-07-15 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 8110e066-f64e-3502-b77f-72d4fa6b09dc | -8.4744 | -51.57548 | 2026-07-15 00:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42e516a1-5b34-3944-bef4-c5b55d7a0c33 | -9.65597 | -48.0967 | 2026-07-15 00:20:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2bc385e0-912b-3f72-9de6-503b233e445f | -10.0786 | -50.14093 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eafb6b2e-a987-3083-a9e7-39b81d0fd019 | -9.74347 | -49.03848 | 2026-07-15 00:20:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2287fbe5-0cf6-311b-b130-1c2d9ac0596c | -8.93997 | -47.61142 | 2026-07-15 00:20:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1ab8b72d-8bb0-328f-ae0b-58e713dad339 | -5.8264 | -43.59946 | 2026-07-15 00:20:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 125b5b29-cc27-39de-9dd6-3f31483a50d1 | -9.54493 | -49.30494 | 2026-07-15 00:20:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 86caf36d-cfad-36bb-a7ac-691feff89089 | -8.48326 | -51.57418 | 2026-07-15 00:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d7959799-f919-3d62-a257-60c3fb8df3ca | -8.94267 | -47.60458 | 2026-07-15 00:20:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e4d1e37f-2b5e-3c36-a2b0-68fec521ba96 | -10.74702 | -43.62254 | 2026-07-15 00:20:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 1f369af0-027f-3d40-b89b-99344b0f22e7 | -11.09591 | -47.79764 | 2026-07-15 00:20:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d35105fc-ceea-32a3-83a9-2e20332b8140 | -11.09774 | -47.81004 | 2026-07-15 00:20:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c06e4a69-a055-36d3-a137-ec8b8d0e61d7 | -10.50427 | -50.15005 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 9f802a4a-9e67-3a2a-8a17-69d7986e8c49 | -10.00618 | -54.52158 | 2026-07-15 00:20:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0eda25f4-23b2-3cf0-be90-1c67e0067d7a | -9.51773 | -47.15424 | 2026-07-15 00:20:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9f409e53-daba-3966-b29a-67d1517682ca | -3.16068 | -48.589 | 2026-07-15 00:20:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b5edc7e7-67ef-39fd-8511-07532179acd3 | -8.85443 | -50.02757 | 2026-07-15 00:20:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b9e3a7ac-22fe-3b5d-821b-8f7b95cf7a3b | -5.3441 | -45.19557 | 2026-07-15 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f3169eeb-54e2-30a1-9d2b-3bd9de7feb94 | -10.5056 | -50.15953 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6aee54d3-6bef-3af4-9ec6-bc73bf817fa1 | -10.06949 | -50.14229 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 43e9f30b-f769-3cc5-9276-8a4b57cd71e9 | -6.03571 | -43.87142 | 2026-07-15 00:20:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1286b40b-7f74-3962-95ad-d0b209957fe5 | -11.40741 | -47.557 | 2026-07-15 00:20:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f91b820-871a-3283-9a0c-f30fbca21483 | -8.73659 | -49.44942 | 2026-07-15 00:20:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| fb46223b-f85b-3898-a490-2c24df233bb9 | -10.06811 | -50.13276 | 2026-07-15 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5930c899-0bf4-3060-86ed-50939543f6a5 | -9.7338 | -49.03992 | 2026-07-15 00:20:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f6d62c8e-7cf9-3880-85d6-5fc52c4e93e2 | -5.34981 | -45.1754 | 2026-07-15 00:20:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 3376057c-41e0-3480-a54b-bd1b96f3bd93 | -9.66451 | -48.10229 | 2026-07-15 00:20:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d5bbf841-810c-3a7a-8e67-0ddfb639a374 | -11.40562 | -47.54506 | 2026-07-15 00:20:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| b8d78651-d90f-31e0-ac98-1e37238a1bf9 | -9.74507 | -49.04932 | 2026-07-15 00:20:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 6e7b2b56-0afd-357b-8c8b-57bb3c0c47a1 | -9.7354 | -49.05074 | 2026-07-15 00:20:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a67a1528-29dc-32da-bf18-e1bec082610b | -1.81892 | -54.4846 | 2026-07-15 00:22:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 72d6a25f-824c-3c8d-99cf-b49f22168a6a | -1.66811 | -54.46234 | 2026-07-15 00:22:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a3fc9c64-72eb-32c8-bbd3-e4743109b91f | -1.65918 | -54.46359 | 2026-07-15 00:22:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 047c49fe-f006-382d-9116-2aa2fa25371b | -1.65795 | -54.45461 | 2026-07-15 00:22:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README2.md)
