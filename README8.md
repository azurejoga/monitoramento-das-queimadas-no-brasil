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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a37b8e8-9058-3426-aaa4-f9c363924612 | -7.49322 | -45.84704 | 2026-08-05 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 926a67fa-a5ec-3422-abea-17287f88ccbc | -9.48744 | -40.36888 | 2026-08-05 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 685eab19-a525-3614-9701-9ad0a74df3b8 | -9.09341 | -37.66154 | 2026-08-05 04:00:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 08e69ff5-2992-3a15-baf6-e96cae3c45da | -7.62328 | -45.31071 | 2026-08-05 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f5cbc40-1248-3f14-86fc-8c9379e962b2 | -4.36724 | -47.77011 | 2026-08-05 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e2555c97-0db8-39c3-8437-8f46c3129aea | -6.90568 | -42.40244 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2af6eea6-d02e-3a34-8cc2-c0f937eddcbe | -6.05614 | -43.8639 | 2026-08-05 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bb15007-1dab-3d34-bfed-fa432c3dd418 | -8.4958 | -46.85789 | 2026-08-05 04:00:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b76b2218-9a8b-3e0b-8bf9-ef2b79a54eda | -8.34223 | -45.97654 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7af341bf-24b1-3356-af10-9d1cd4ac50b9 | -5.78956 | -45.04754 | 2026-08-05 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2b1ea5d-fa33-3968-b03e-e6464574f9f4 | -6.15099 | -47.1803 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 102dae6f-a630-31ca-8dc1-08af7ad181e8 | -3.24841 | -47.92625 | 2026-08-05 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef21b140-81ed-3c79-acc0-2f72532a269f | -5.82692 | -44.13646 | 2026-08-05 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2a5d10ba-49ec-359a-8196-682bc744d525 | -7.22416 | -45.77163 | 2026-08-05 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ccd0c51-5746-390b-aaf1-0b141ce7840d | -6.14694 | -47.17316 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c6b7a702-3daf-374b-8ff5-6c5c5ac577e3 | -8.34599 | -45.982 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c0bf4180-77e7-3376-8eac-abc064f5636d | -6.00831 | -47.4066 | 2026-08-05 04:00:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 600d4954-4885-3670-bb2f-2e9102668fbc | -6.30657 | -43.61966 | 2026-08-05 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a93a4608-d302-378b-82a3-8f5d0adb88eb | -3.02808 | -48.41407 | 2026-08-05 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 680ee4c1-d6de-3dde-b13d-c318fd82c6de | -8.56391 | -36.93985 | 2026-08-05 04:00:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7ad71de-0d08-38e7-82ab-d63ff4e7144f | -3.66937 | -49.47341 | 2026-08-05 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18a22d24-973b-3336-8c82-f659aa45a57d | -3.6685 | -49.47832 | 2026-08-05 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 017fe607-b9ee-3769-82b1-e16ee80d43e3 | -8.35058 | -45.9828 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 04bc8b09-0544-3cd0-b401-15b5e467ced4 | -7.18199 | -40.16903 | 2026-08-05 04:00:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0d5c085-b0ef-3557-8c36-6705764261aa | -6.94386 | -41.92204 | 2026-08-05 04:00:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ae0f415-7fb0-3846-81be-20c85b74e37f | -6.6463 | -43.90934 | 2026-08-05 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56f50eb5-5793-3a6f-967b-8d1a90914755 | -8.33681 | -45.98046 | 2026-08-05 04:00:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 20852772-adc9-3e29-be46-6e3e4c320ac9 | -6.30632 | -43.62296 | 2026-08-05 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd6e3c72-e19d-36a2-8dad-4207077aa25b | -7.45112 | -44.89257 | 2026-08-05 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffd8bad9-c75e-365c-b4ff-93af9435c4b6 | -7.22876 | -45.77245 | 2026-08-05 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7643382b-8fc1-3dc6-a233-4f517268fa82 | -7.50363 | -49.74641 | 2026-08-05 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a6b31184-5e66-358e-8c76-3c8195ffcb66 | -9.48018 | -40.37136 | 2026-08-05 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 16bbca6b-87ef-3f7f-9808-333542ec5f9e | -3.99158 | -48.39545 | 2026-08-05 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3e6d752-c590-3bb9-a4b8-4d60cd97e015 | -7.22712 | -43.34789 | 2026-08-05 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3ec584a6-eb47-3152-947f-f93167586eb0 | -6.30598 | -43.62321 | 2026-08-05 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db18fd26-590b-37c0-b872-3eec76d15fb5 | -7.00323 | -45.85349 | 2026-08-05 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fef4d8d-bca2-355b-bc61-84c3f4404593 | -6.90494 | -42.40691 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5cad99a5-a81a-3937-89d6-e74b452bf5e3 | -6.48133 | -42.22432 | 2026-08-05 04:00:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e69f464-f0da-3ff1-ade0-019cf4ba5cd4 | -3.16506 | -48.13736 | 2026-08-05 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 735d505d-516a-37f2-886f-2af6827dccc8 | -6.93231 | -41.92431 | 2026-08-05 04:00:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 21ba2e9f-7613-33d0-91ec-a75641fa110e | -6.89153 | -42.41853 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 36d35feb-1d57-32e7-a21e-afc004bac144 | -6.24382 | -47.14712 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d4b06fe-37f2-3f9c-ad64-a76f0595ff12 | -3.03034 | -48.41092 | 2026-08-05 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6d669e0-6b61-3f66-a83f-cb4e46ca9fd4 | -9.48352 | -40.37191 | 2026-08-05 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4a958eb9-e8d3-3cf2-a1eb-adb782c49a0e | -4.36788 | -47.76638 | 2026-08-05 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 680893da-9b1e-3698-bbae-352ae0d48474 | -3.16451 | -48.13876 | 2026-08-05 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a67fe37c-0b07-3ee7-8b23-a5341ddead02 | -4.28041 | -48.03971 | 2026-08-05 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| feafbe02-8acf-3570-86ea-174d335e5315 | -7.22775 | -43.34603 | 2026-08-05 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 075acc6b-6d8a-3a28-9650-288bf0c0c76a | -7.5028 | -49.75082 | 2026-08-05 04:00:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1ad4b2a9-23b8-32a5-8738-3bcf24e36c3c | -6.9316 | -41.92851 | 2026-08-05 04:00:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 84d82589-946b-33ef-a565-467ae4b65fc5 | -6.90345 | -42.41592 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cb9ad740-d7be-3469-aa6e-7dd4117639f6 | -6.11502 | -47.89374 | 2026-08-05 04:00:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b503d5ff-c5f4-35c5-8af7-064266f3dd6d | -6.09294 | -43.67352 | 2026-08-05 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3be4e05c-6993-3e79-b19c-93a6706e5661 | -3.66397 | -49.47921 | 2026-08-05 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abfd5779-c6a0-3cb2-95e3-31a71efad06c | -7.62695 | -45.31592 | 2026-08-05 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b78774d4-756e-3bc8-b5bd-09be52106b84 | -6.90047 | -42.41077 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dec050c4-9e4c-3cf5-a5d5-b4f31435d876 | -4.79971 | -40.04239 | 2026-08-05 04:00:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e45aa19-6d43-3d2f-9944-af1828420fb2 | -6.89601 | -42.41462 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 2127529c-35b0-3f8c-b0fd-7ac7f5ecedc3 | -6.50347 | -44.701 | 2026-08-05 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fae89c53-d17f-3819-83cc-cf4a00be17b4 | -6.47762 | -42.22374 | 2026-08-05 04:00:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5662ce82-7870-3235-935b-7182119573b2 | -6.89973 | -42.41527 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| be616c57-9fa2-34ca-a719-fa3c3f366e52 | -6.24151 | -47.14838 | 2026-08-05 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7deed410-6974-3625-855a-9edfa116ce1d | -7.15125 | -44.71841 | 2026-08-05 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e4e0d60-c958-30a6-8abd-e3cf41366bc7 | -3.66564 | -49.46942 | 2026-08-05 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| df990f24-f10d-352e-8cc2-b125406aa75d | -7.22154 | -49.59411 | 2026-08-05 04:00:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 231cf96a-bf2a-397f-be5d-a2cad8c5d5ff | -9.06527 | -46.04809 | 2026-08-05 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3559535-ac3f-36b7-9393-39e659f239a2 | -6.8945 | -42.4237 | 2026-08-05 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a6df1a0f-9062-3418-b771-64ad4c0edd3d | -6.93522 | -41.9292 | 2026-08-05 04:00:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c688dddb-e0c6-3a9c-9b52-dbda02897f43 | -10.45848 | -50.23205 | 2026-08-05 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79d0b198-6c30-37a6-a8d1-552842ee4de8 | -14.26724 | -45.30078 | 2026-08-05 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3ffdb31-fc10-328c-b279-62e0af3fc689 | -15.02857 | -42.38541 | 2026-08-05 04:02:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c8bed975-93f6-3dd3-a845-6c4c1a65336c | -17.33935 | -42.63474 | 2026-08-05 04:02:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 028417ea-166c-393c-859d-1a89d47f1241 | -16.22104 | -45.49063 | 2026-08-05 04:02:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52242acd-f92d-30d7-a172-213c11200896 | -13.43494 | -43.84855 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf79b694-2ee1-347a-acb1-34e83425a6d6 | -10.91861 | -50.41948 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d4eae82-982e-3f9c-bf90-7fd1b7c07faa | -10.91856 | -47.32401 | 2026-08-05 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44dcf389-1015-3af7-9bcf-8efa8e040478 | -10.60589 | -46.37714 | 2026-08-05 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d5c9ea1-8af9-35eb-91db-6e9365debb03 | -10.60908 | -46.38027 | 2026-08-05 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 070f6d52-ef07-30c6-a2e1-47d0b21f6ed4 | -12.43563 | -50.5199 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40c80ca3-15ca-3cbd-9ee0-84426a59622a | -12.4471 | -50.37686 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff4c1e49-c5d2-3404-9546-86458e49bbbb | -12.5832 | -46.95037 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 92108a58-c74b-3a51-b6d5-496c1c531ec9 | -14.17619 | -54.40638 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10f46e4c-8f8e-3def-b49a-8d28f445e47b | -14.34849 | -47.51678 | 2026-08-05 04:02:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4634c825-bdf7-3e6f-a402-234a6b76f056 | -12.58581 | -46.93643 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e2f3fdd-105f-33ee-ac00-4adfe01a8d90 | -14.19317 | -54.44031 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb56c9ef-42de-3ea2-8aab-c531a7359e8f | -12.49376 | -45.54052 | 2026-08-05 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f43c394c-74b0-3b9a-8040-6daf38945568 | -15.70281 | -46.75483 | 2026-08-05 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ee1a4d5-b411-3328-9542-60ee68097750 | -10.60455 | -46.37948 | 2026-08-05 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 345173d6-19f4-3cf3-bbc9-ccb9bfa0543c | -14.18159 | -54.41491 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 609d7676-20e5-3034-9607-e82c3ff020ec | -14.16467 | -54.40319 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdd41bdc-cf0b-34cc-8409-6bac39e8957f | -12.58776 | -46.95114 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9ad240a4-05fd-30a0-91c2-d40265f2e325 | -12.59746 | -46.92437 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 512cad5e-d69a-36f2-8fe7-d509f2b0a462 | -12.59307 | -44.15809 | 2026-08-05 04:02:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 064d8b02-1027-371a-8887-48e9a114846e | -14.71742 | -47.14682 | 2026-08-05 04:02:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f8f5b8b-0b23-3f9d-9598-6a4792c0555a | -12.45192 | -50.37514 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b052e22b-e8f0-3cba-8ffa-79920089a68c | -14.16793 | -54.41048 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0691e39d-a7c4-39b0-aba4-ab9a12a5de59 | -12.43632 | -50.51839 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff205b72-7d10-3cc6-839a-2ddd2c8baeaf | -13.44098 | -43.68005 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 220e97c1-381e-33de-9868-e881b8b3995d | -10.91413 | -50.42067 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86885945-2743-3f39-b0a0-55804b27fc56 | -11.54838 | -47.70893 | 2026-08-05 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README9.md)
