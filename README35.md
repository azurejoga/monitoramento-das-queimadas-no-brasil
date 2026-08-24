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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1085e805-1ea1-38ab-bbfe-17404336ea64 | -12.1188 | -50.61868 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fd4b1c46-2236-364c-bfc6-9ae7ed4388fc | -9.03059 | -50.75091 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 18b17c6c-df3a-3614-acb8-18b9b8f5d2f8 | -12.09283 | -50.58925 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c25a3db-9328-3f47-8b8e-af63df497ae4 | -12.89409 | -48.47017 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b56f6da-77d2-3132-aa99-7efe8bc0ad35 | -11.90871 | -57.12381 | 2026-08-24 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf4049c3-1ab6-39ac-ba3b-82c55a333027 | -13.69177 | -51.83728 | 2026-08-24 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed73b7a1-8f2a-3ae9-8f89-e2a008a6e840 | -8.37561 | -46.47195 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21880da2-c588-3ff3-8670-6e937ee8fd97 | -12.86769 | -48.47836 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 345e8f27-0468-3c7f-8525-1b98a76c1bcf | -6.81348 | -58.65249 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a2c875ea-9c1b-3b41-ae0b-6fa5893a3e2f | -12.10775 | -50.60242 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4dd695ed-9ee7-3ba8-ac1e-0cb4fa2c0482 | -14.3395 | -51.75923 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f439a4a7-509c-36ff-8dae-ac5573620176 | -12.10885 | -50.59546 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 122d1aac-6b50-3cd0-a24d-c4afe995c79e | -10.53116 | -50.77854 | 2026-08-24 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01ee3829-f017-376c-990f-6fe9bdec1f4e | -6.54551 | -56.1769 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af788b41-840e-3e59-9686-9f50e115d326 | -18.69488 | -47.47319 | 2026-08-24 04:46:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 19a5325c-ab68-30fe-87bb-1c8e85841ace | -12.74945 | -48.37293 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c754d819-5ecb-3985-ae34-0e6298814bc6 | -12.72096 | -48.39522 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28bc0631-05a8-3622-9c74-b2d1fede13dc | -11.155 | -54.00793 | 2026-08-24 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f845f34-49db-31d6-95b8-4357c242c4bd | -10.73161 | -47.9763 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a8dc138-d509-3abb-9b02-a84a1cdedf7c | -12.08952 | -50.61031 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e4eca2c-d503-38db-8a71-6a4c83fd3ba7 | -12.71504 | -48.41073 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76a5fa3c-cc4e-382c-ba41-a38e396f5e2d | -8.9269 | -48.54391 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d69d565-3034-3da1-b8b1-b7e64be1cf55 | -12.71561 | -48.40694 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b4eb8de-5b06-3c58-a467-05e5afa21342 | -13.21353 | -51.47025 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a074992-0021-3379-b6d7-00984f47250c | -9.17689 | -58.07356 | 2026-08-24 04:46:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0f8fe5f-98d3-3626-a054-6dcbdf829503 | -14.43801 | -51.80117 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4ec3c83-068e-317e-b47b-083fcb02f381 | -11.91242 | -55.90522 | 2026-08-24 04:46:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 759691b5-a6ff-39b0-aecf-b77ef0d8c863 | -6.7391 | -59.66376 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ed23a2-4b80-38d7-9138-777a9cf42854 | -7.68592 | -50.74562 | 2026-08-24 04:46:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14e9e67b-f607-337e-851b-69f97df5b01d | -12.60845 | -52.46166 | 2026-08-24 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19789ae1-05a3-3099-88f6-2e201b1efc6a | -10.83049 | -50.56216 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eae9d8c9-2989-3d4d-b088-b5b5252cb2d5 | -8.5573 | -54.84473 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 496732e3-494e-3480-bd8d-a7f4294f3e96 | -12.09615 | -50.61139 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdd492e5-f6d4-3d1b-afff-ba3d1cb85be2 | -8.31446 | -47.58686 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73b5dfa2-b2ae-36a6-a975-4436cc2caa3a | -11.3895 | -50.7207 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e1417c3-0a8c-377f-be80-681782c077a7 | -10.81966 | -50.95172 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91f70a1a-87c7-3444-9045-8a965072e5b8 | -14.31593 | -51.8429 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5f1b811-142d-3b99-a7ae-8b0ee9f91a0e | -13.16461 | -51.39323 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8ae7ce68-ec2a-3de8-8f21-32a2633b4d7e | -14.78686 | -48.78102 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f44ac69b-11d8-3182-85e8-f2e9b7e5c7d0 | -14.78394 | -48.77621 | 2026-08-24 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1a15029-1c4e-3199-8c3e-2018a7ff9408 | -13.19528 | -51.47811 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ddbc648-a82e-3626-8c69-2068b81e54fa | -12.58563 | -47.94703 | 2026-08-24 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de1038a9-f984-3759-a39a-8d60e70a5f91 | -9.9546 | -57.86015 | 2026-08-24 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14749e47-d9ee-3b61-87fc-c8665ff00f78 | -14.32568 | -51.76056 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 376c3f9c-5121-3c92-a98d-94bce17c3bd4 | -8.30973 | -46.89587 | 2026-08-24 04:46:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6600384-33d5-3c0c-bf28-5fc8fbd1c583 | -11.85765 | -51.70459 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f235c74-4847-3c68-8290-0d2b9ae1a6a3 | -12.11825 | -50.6222 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4ef107ed-b17b-3516-bf1b-0a0402ddd763 | -9.036 | -50.8234 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 952ab975-197d-3e1d-a9ed-0c2c3442863d | -13.89512 | -54.04028 | 2026-08-24 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40587abf-dd6b-3047-bd39-cae258e00b3e | -18.32113 | -47.20496 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5053e3da-deb9-3be9-96dc-7d087b69e806 | -9.03212 | -50.82639 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad25a0b6-2eaf-3a79-8f13-bee0851f122b | -14.41378 | -51.78249 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7164b6b-bc6b-3142-ae99-390b916d56e7 | -8.10829 | -47.49322 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0a7945-9406-3a1c-b1f3-503c3ae6c274 | -11.41403 | -45.12698 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86517835-23f2-3ec1-83ef-28ce7647b3f1 | -12.11383 | -50.60703 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e5ac202-e5f5-37af-b294-5a57d8dcd563 | -9.0037 | -60.4199 | 2026-08-24 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1fda4b2-2e36-36fc-94c2-492188723d33 | -10.27128 | -50.38216 | 2026-08-24 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07219e27-1de5-37dd-b5c3-de05a4f8f1f3 | -8.55074 | -55.28474 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53f36fb3-3769-33ec-b3c0-41c1bfb05cd5 | -12.10444 | -50.62357 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8df8a51f-d11e-3e66-b360-70906cd44a7b | -12.10941 | -50.63522 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57293283-dc2b-3ff9-ab84-1c7c68d034f7 | -6.60663 | -58.38473 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fd5451d-962e-37a6-9405-00c5caadefd8 | -8.54751 | -54.85086 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5702647-0210-3069-b5ce-92b8b74dbbc0 | -7.78194 | -56.28867 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b13cbef5-460c-30b5-8e46-6d069f5a0533 | -12.74162 | -46.46958 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcbc9349-6db9-3309-ad82-dd85bf49f78c | -12.86359 | -48.48181 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 157f759e-6407-3d28-ae6a-584e1e66a365 | -6.79634 | -59.59074 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5ccb765-7e62-3e1b-a8b6-7d1761f0643f | -15.51578 | -49.83537 | 2026-08-24 04:49:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39aa66f7-798d-306b-ae86-9ed8277f631c | -15.54302 | -55.14439 | 2026-08-24 04:49:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1e8f348-411a-33de-bce7-d2762811be7c | -15.29124 | -52.81302 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba803468-bdb8-39c4-a560-2c6c19495259 | -16.38421 | -51.82201 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7d1d6c02-7c3f-3c2a-a22e-213e5dd74654 | -15.26675 | -52.85774 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86113db3-cc0c-3d77-b1c0-644324aa016b | -15.34945 | -52.7852 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ef25e0b-7d3f-3aa0-bd67-9833930ddbdb | -16.85911 | -49.44487 | 2026-08-24 04:49:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b63eafb5-2625-3c73-b144-be58ab2fdaae | -16.04734 | -48.00345 | 2026-08-24 04:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03117070-ffdc-37dd-87d0-aed8e260f9f3 | -23.00175 | -49.37571 | 2026-08-24 04:49:00 | NOAA-20 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f150f272-528c-3cbe-a93f-6eb5a389eac2 | -23.82568 | -48.71836 | 2026-08-24 04:49:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 247e0222-d671-3777-88fa-e6bfac2dd721 | -15.33357 | -52.75628 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ad9e223-82bb-31c6-8683-f2a3fe4ae644 | -16.41838 | -51.84254 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1a118d3-a42a-3134-aa06-89f40b37264a | -15.30344 | -52.82264 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec8c82df-3d42-325a-8ca6-9a06907799f6 | -16.05769 | -50.44304 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63f8bc3d-269b-36fa-8c52-eaf3e61268b6 | -15.2706 | -52.81303 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3803e61-a33b-3411-b03d-ac37f9eed8ef | -16.08747 | -52.34241 | 2026-08-24 04:49:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff2c8ca8-21a0-33fa-9da6-c436eee3d121 | -15.49402 | -52.90372 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20bd8ab8-f095-344e-8b88-2177f11dcd02 | -15.26485 | -52.82716 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5815bfd2-3412-36c3-8820-d91e297571a4 | -16.41872 | -49.92093 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdf3d083-9fbf-33e8-a764-dc19ff87211a | -22.94921 | -51.78279 | 2026-08-24 04:49:00 | NOAA-20 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49b4d006-7860-3a4b-9618-165ce1574ca9 | -15.35339 | -52.78216 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5345d85-6f69-3f80-9c2a-1566bc229a11 | -16.08805 | -52.33882 | 2026-08-24 04:49:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e259746f-3481-3cde-824f-215a88fa5078 | -16.41916 | -49.92251 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1bcc323-6915-35e0-a8e2-4706fa99851c | -15.26436 | -52.87239 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40a5a58f-48b0-3946-a011-bfcdb584efb3 | -15.2873 | -52.81608 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f581c422-9e3a-388f-b8fc-dea99d6cee46 | -23.12569 | -48.68273 | 2026-08-24 04:49:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 331ea810-edbd-3c3d-a797-b9a6a4d5f1f9 | -16.38047 | -48.98563 | 2026-08-24 04:49:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a1d9605-7098-3afc-8749-18a6cb8a50cb | -14.98282 | -52.68138 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d9bff03-0905-3421-a90d-ba5dc0c3663f | -16.40465 | -51.82178 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc594bf0-1f52-3b68-ac21-469d5613d3ad | -17.42254 | -48.84039 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f3e896d-d70c-3e5d-b877-5ab188d933ce | -16.40021 | -51.8284 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c15eb23-d3c9-3a1a-a62c-3f0fc11075f3 | -16.39803 | -51.82067 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04275c1c-8a04-3b1e-ae5d-7d0a915143f9 | -16.39359 | -51.82728 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8474e80d-d038-3a13-826f-bc75202f2070 | -16.30732 | -53.16814 | 2026-08-24 04:49:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
