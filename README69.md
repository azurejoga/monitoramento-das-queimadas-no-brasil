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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88ab8f1c-adfe-3a40-9bed-193813cd0973 | -17.70732 | -44.494 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11bbca3e-e128-37df-b37a-48e02d1b382e | -14.11013 | -51.72063 | 2025-09-06 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66394aa9-b612-3175-b759-502d960b7b3d | -13.002 | -48.05089 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 447aede5-3df2-36de-b646-d0f32c77d525 | -12.96714 | -54.79349 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58f13215-f8fb-3294-97a5-a42aca8728c4 | -11.0137 | -45.92266 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51415f6b-5bd9-336c-90b9-036fce5677ba | -12.50437 | -53.87073 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 108381de-291b-3787-a9fd-15bd9ce776dc | -13.06497 | -47.10309 | 2025-09-06 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d9105d4-c70e-320b-912f-6e8fcd7562bc | -16.59843 | -50.53319 | 2025-09-06 04:40:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6008b5b-3133-368d-a6bb-e7161e795a5e | -15.8431 | -52.29025 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b37f4f59-3bd4-3a05-9517-aa2d1e32b8a0 | -9.98694 | -51.62835 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 221c5980-6653-3221-9427-af3ec34b1ffa | -11.64013 | -52.22863 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c0e113-4b03-347f-b28e-4d9d527048e7 | -11.13576 | -46.34674 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8be6e8a1-7044-39ac-8aac-45a5dd5547f3 | -17.70204 | -44.49804 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f2ca4fa-dab1-310c-a93e-4163d839627e | -14.17651 | -53.06815 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd2855e8-92cf-3461-bf72-5cdb7bcf1209 | -14.71801 | -55.93011 | 2025-09-06 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 787b881d-b7a2-3421-a07b-4cf99469ab95 | -11.58405 | -52.189 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f44488a3-9ffb-33b3-ba67-3272d42e97fd | -14.58324 | -48.0022 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5138090d-314a-3ccd-bc74-2f50041299d9 | -12.99597 | -54.83408 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c3e1cc6-f2f3-3955-9aae-5c8d19ba694b | -10.08943 | -48.08445 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d27a619c-11f1-3aa9-b7c0-6c73c21683e9 | -14.59119 | -48.00237 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eba4571d-24f1-3304-b308-16a6411bf9e9 | -11.10508 | -52.04627 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31bb7c97-f289-3b58-a89c-5192c174845b | -12.98718 | -54.81829 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4036259-f18a-3b6f-884e-378455a673d6 | -12.93812 | -48.04696 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac67c5b2-1df5-3c34-b1bc-2874eaa4ab86 | -11.21478 | -55.0214 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83e46fad-8516-3774-83fb-88d9fba8134a | -12.95768 | -54.78948 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b87dd2cd-4e90-3478-8bec-8269c0c72283 | -12.0159 | -47.78233 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0371c20-be41-3d31-b198-dddb275b7a8c | -17.7582 | -42.51849 | 2025-09-06 04:40:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 64239093-21e3-33d8-87f4-341d26c892f6 | -12.51641 | -53.84301 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c33fa09a-8809-3d9e-8d4e-39c541f87d37 | -13.01618 | -54.82824 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6b4230d9-309f-33cb-8dac-b3861a2005a7 | -10.4611 | -53.61967 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f525aa3-6c7a-37d8-a160-70f4b93ca6b5 | -14.56692 | -48.01233 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c70406c-370a-365f-ad5a-d940969e0174 | -12.00326 | -47.77723 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3447d1ac-1f7f-3460-abce-0caa8f323b7a | -15.1815 | -47.99171 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26540895-d837-32d9-b4f2-463b297460f3 | -12.9989 | -54.83933 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0eab1bc8-5a0a-3eb0-b364-4a7964fa7ef2 | -9.70679 | -51.10592 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c94ed12-2eb7-3295-b2ee-fe0fba4a5cdb | -11.09376 | -52.05188 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e30f9420-ae8d-3e50-895b-d5a1ea5a7ee9 | -10.87706 | -55.73208 | 2025-09-06 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ca05659-2dc1-3273-af0d-66078d9fb7aa | -10.77219 | -47.7496 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d33c0fb-fbe7-366d-8ba3-759ae83dcd2f | -11.65206 | -52.21935 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f3631da-ce4f-36a0-8a4b-7070fc080f4a | -10.14039 | -55.15776 | 2025-09-06 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f7a772b-f93a-34b3-883f-03e3dab6dd21 | -11.60514 | -52.16611 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e92e2054-90dc-33de-b001-daf612e243f2 | -14.3382 | -60.32638 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 976792f1-728b-35c0-a35e-cf7204f5728f | -14.84342 | -48.19153 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af92d68c-dbf0-3813-b6c7-06a3d2763fb0 | -9.68842 | -51.11382 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99835133-fdc3-31b1-a309-92e456fc4ab3 | -12.84918 | -48.01395 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6b24b5f-6b19-34f1-bae8-84af909605c7 | -12.49008 | -53.86828 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d72d55-bf59-3839-bac3-4c878530a206 | -12.99224 | -54.83342 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7575098-7818-3967-9e51-9a0956e47cae | -15.36226 | -46.41797 | 2025-09-06 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 095851ec-56b9-31a7-aff4-154998724652 | -13.56957 | -48.12156 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c59118b-74ac-3a5b-92f3-3c52022e2028 | -14.96309 | -47.59458 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c247561e-746c-31ba-b014-7c5ac38be5b7 | -12.48863 | -53.85521 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc6edfd3-1987-3212-a156-68a0f4089c29 | -15.85407 | -52.30703 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce6f8560-f9b9-331e-8f25-02aa333174fd | -9.84547 | -48.83574 | 2025-09-06 04:40:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7116190e-1c12-33a1-ae50-e7b39e271880 | -16.32716 | -52.94832 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 38bc71d3-6058-3d2f-a82e-384435998308 | -11.02836 | -52.04857 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3afb5f7-a76d-3914-a48d-2adc8dddc21c | -12.959 | -54.80382 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61520c48-9ae5-39f2-bc93-b50fa38e529d | -15.17538 | -52.40691 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b23ff34-7c3c-362c-b2b4-e8d04f1b8376 | -12.53614 | -48.07684 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85c34ec0-6747-3e6a-84b2-6f624426f52a | -15.98197 | -42.38808 | 2025-09-06 04:40:00 | NOAA-20 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7f150605-779d-3cfb-a13b-8a8fee4bf6e0 | -13.01245 | -54.82757 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d77f25f5-a9e2-3ad3-ab5d-7b009fe3db44 | -14.96814 | -47.58599 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36cb7efe-07c1-3885-b3cf-beab5d281093 | -12.96006 | -54.77597 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 824f49c1-ed0b-3869-a311-4a90089f85fc | -12.97733 | -54.83074 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f64455b3-2763-3a10-917a-7b6a5d210231 | -10.46543 | -53.61606 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe90911e-8025-37fa-9129-020c313bd816 | -14.33733 | -60.32603 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 457f845d-58e6-39fc-9394-10335fa03518 | -13.59287 | -43.35156 | 2025-09-06 04:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 769c2f28-cb3d-3fd0-8092-1c77a1dc424e | -15.73063 | -53.60244 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf281cf7-d10c-3947-b2ca-f24b858b0022 | -14.43719 | -53.19003 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e680f888-6393-3bda-b72f-f2b50d5bf09a | -14.34268 | -60.32611 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fb2bbe8-1152-3899-8f1e-7da7457043a0 | -15.21469 | -52.3542 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7251d79d-d4b5-328e-9f30-414e820f2abe | -13.01597 | -54.85178 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0cd4b47d-072c-3035-bfee-87d76318a0c3 | -13.0154 | -54.83278 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 53e456f3-b34f-312b-b933-7d532b712c78 | -14.28585 | -53.04419 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf09006-1242-379d-bb3c-5f45832723af | -13.8433 | -46.27025 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 425c2cfa-88da-3254-b24f-59a509a0ae45 | -10.22369 | -50.52676 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7289f6e4-61b2-3626-85d4-a7b11356b875 | -16.91615 | -45.74787 | 2025-09-06 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc0ef1d5-9a5e-34b0-a059-2f000f6a68d8 | -11.54461 | -47.32036 | 2025-09-06 04:40:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b227b49-8a45-3520-b86a-aff0d0d8da79 | -11.5928 | -47.73982 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b3cbfc4-9c4c-3c6b-a037-73c36e08ac35 | -14.37342 | -53.02409 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b1c01c5-519e-31b9-9ab5-c2ed879f94dc | -10.06641 | -48.07278 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62bb1a59-bd76-3f8c-aea1-7bdbb91203f2 | -10.31502 | -46.41339 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1a940fd-1c5f-3752-8437-cb8a599b6360 | -9.68385 | -49.29165 | 2025-09-06 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a40477a2-9935-3d98-97b7-49c7bff7d417 | -9.45946 | -60.50839 | 2025-09-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53a723c7-d2bd-36f2-b1ab-1e64aaa49e60 | -10.21698 | -49.72577 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61a46ce5-593e-3547-9e42-88f28d0252da | -11.63132 | -47.8 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ac1a555-b5f0-3391-a027-7aaf6fc1e878 | -10.44735 | -53.61304 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a15a1a14-1f23-337d-b12d-f1551508d3ca | -9.71341 | -48.9894 | 2025-09-06 04:40:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a1ef10b-6399-35e0-ad83-86b39fe52716 | -12.7304 | -45.09684 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4a483dfc-d03f-3572-bb40-9b5f583c81a1 | -16.29919 | -45.68993 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7059e36-95e1-3148-9323-476d45f69ad8 | -15.84525 | -52.2981 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e054247-32fa-39ab-ae11-9306e698a107 | -10.74262 | -46.33932 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 406eca37-e9e0-3518-8045-d2fc35741fe9 | -9.56213 | -53.58892 | 2025-09-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70b6919c-4e7d-3204-9184-40104e880ac8 | -14.33152 | -60.32835 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67c8e7bd-405d-3ebd-a648-3578bb561576 | -12.18827 | -53.89724 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81efcb96-448a-39a3-bd18-d67a255c4d4f | -15.14579 | -48.16424 | 2025-09-06 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec467c07-ef9e-322b-b06f-aa23dec5ee95 | -12.47721 | -53.85752 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ae5704-fa8f-3642-bb33-69672ba4de35 | -9.72302 | -51.06862 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e330f9fa-e040-3ed7-ab61-92fa4283b007 | -10.31369 | -51.453 | 2025-09-06 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d165f21-7f31-30ba-a4d5-1364aab144b5 | -12.00746 | -47.77357 | 2025-09-06 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67f176d7-89f4-3623-9c06-19976564e66f | -12.50507 | -53.86658 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README70.md)
