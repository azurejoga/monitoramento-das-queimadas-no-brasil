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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53986308-a1ad-3b98-816b-c5d8e95a7fbc | -5.8279 | -52.080101 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9629b700-1b05-3a15-aa40-36f9bcf52e31 | -3.3826 | -50.454899 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25ad36e1-e140-3841-b6d7-d960e1fd0b15 | -8.5622 | -50.152401 | 2026-09-18 01:02:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28c5b1d6-8b1a-39eb-bcba-1e39ad937bc4 | -13.601 | -48.2883 | 2026-09-18 01:02:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 18600319-c63b-3d44-9f2a-cfb2debd49f6 | -12.6185 | -50.8699 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb0d66c8-8f9b-3492-bf78-ecf4bd4cffdc | -5.1754 | -56.185699 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e551dfb8-9096-3eff-8aac-b6d8eb2af9f1 | -12.3321 | -50.751301 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10e4cae6-eafd-3ac0-b425-c393be5b7537 | -12.3303 | -50.7435 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2220586f-2ae6-3885-982d-d70c5c3c22b1 | -12.4598 | -50.679199 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e028b06-a14a-3a19-aa33-f3fc5fb4d09d | -9.397 | -46.853401 | 2026-09-18 01:02:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8eecf955-6cbc-3994-837e-9ed7213fdd94 | -6.1223 | -44.0327 | 2026-09-18 01:02:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52978895-59ef-341d-aca1-53516a0846c9 | -6.3589 | -58.293499 | 2026-09-18 01:02:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7137958b-ff94-3ed1-97aa-d5d5dfed163c | -5.7606 | -45.077999 | 2026-09-18 01:02:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44e671cd-f854-334b-8d80-026f80fdab51 | -12.4733 | -50.692501 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83a5b1b4-5b95-38af-823a-4165f2f861ac | -4.8802 | -56.065899 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c2a9a2a-4a1c-365f-9ea2-bf32ae0f40e3 | -2.9023 | -54.188499 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 988ed9a3-e570-347c-a683-024a2690b9d9 | -12.4091 | -50.683201 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9c7b321e-80d9-3e33-ad47-61696385703a | -3.6972 | -54.548 | 2026-09-18 01:02:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d343b53e-abbc-3386-8232-76ea35fb3184 | -4.5651 | -54.9132 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85300f1f-e48b-3d50-a527-4c5640e8a36e | -12.2734 | -50.765499 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f86f879e-9f2b-3486-9811-57ef163df96f | -3.4498 | -58.2029 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22b18986-9a2f-3f09-9401-cd650388daab | -3.4772 | -54.7127 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c75e373f-5184-33db-b9ef-bfa33eacf41f | -19.1884 | -48.778599 | 2026-09-18 01:02:00 | METOP-C | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23ec4fff-a8b4-386b-b7aa-0d335f070224 | -9.9205 | -46.553501 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9a52b22-2481-3ccf-b06d-dfa122048a96 | -3.3197 | -57.8563 | 2026-09-18 01:02:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24bf3a12-3ae3-37ec-ae2e-7ef9d95ac641 | -5.8928 | -53.511398 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da782533-401b-3b26-a791-bf89967188fc | -12.6221 | -50.885201 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b3ddef9-299a-3e76-ab5e-61e322f8ac2e | -12.3987 | -50.726898 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4c97327-227a-3a2e-94f6-f2cff09ca68f | -12.3474 | -50.772202 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5371c76f-18bf-3d4a-8a5a-3d6685c27d6e | -3.4724 | -54.692101 | 2026-09-18 01:02:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 410b27b1-8e7d-38dd-b683-119cec34b09d | -16.4042 | -49.956699 | 2026-09-18 01:02:00 | METOP-C | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 86d93a72-4bdf-3c36-bc6f-7e484b48779a | -12.4054 | -50.667599 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92b94d67-34bb-3167-9b6e-fa0085913bb4 | -12.4072 | -50.6754 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a11a9e7-e1dd-3240-bc87-51095b521fa2 | -12.1803 | -46.988701 | 2026-09-18 01:02:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6f3c52b-3a53-38a1-a970-10d07ffdab1c | -9.5578 | -45.409599 | 2026-09-18 01:02:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18d6e0de-88c0-31cf-a4de-1d1b6a0c075a | -4.4282 | -55.0802 | 2026-09-18 01:02:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8256d90c-240b-3bd6-8639-1dacbad8c24b | -2.8991 | -54.1745 | 2026-09-18 01:02:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fa3e202-f8ae-39c5-9de6-0b6272a958b6 | -14.9376 | -49.9212 | 2026-09-18 01:02:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 50c49520-ba0b-32c1-b31b-1ef349d76ec2 | -12.3376 | -50.774601 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3f9f059-f4ad-35ad-b42b-be1a890dc704 | -12.458 | -50.671398 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a25ab63-423d-3646-9c6c-69a23defd0c2 | -4.5768 | -42.973301 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36f8164d-ebad-3e90-8739-6bc73f192b8b | -13.2599 | -46.918499 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 56d0794f-cbde-3a91-8bd8-dbfb2f6353a9 | -12.4678 | -50.668999 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5019abdd-a525-3c36-82a9-bb1187698b1f | -12.2114 | -53.2187 | 2026-09-18 01:02:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26af5f89-22ef-336e-bd1e-fb718592196c | -12.5378 | -47.093201 | 2026-09-18 01:02:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59b040cf-5bcb-3fb2-9607-c4cd2d9b919b | -12.3816 | -50.698101 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4911e10d-c0b8-31ee-a124-ce31a5313981 | -21.4636 | -48.679798 | 2026-09-18 01:02:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3a3b8269-aa48-3d93-868d-9e06a37eb060 | -3.3313 | -57.8619 | 2026-09-18 01:02:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35b48f46-3e80-32d2-b9a3-c593b603160b | -10.9927 | -57.057701 | 2026-09-18 01:02:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 429be779-0d4e-321b-808e-ad4585e2f3e5 | -4.8818 | -56.073002 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b5d633-b750-39a6-8267-820d9eeea6b6 | -6.5147 | -49.8806 | 2026-09-18 01:02:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 372ac2d9-503c-3fc9-bfbd-a371c28eaa57 | -9.9492 | -45.3269 | 2026-09-18 01:02:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca30877-fd71-340d-a5f8-dc7c4b682d4c | -12.1706 | -46.991199 | 2026-09-18 01:02:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dea0850-8b12-30cb-8926-68c3d9e3ccee | -11.3009 | -43.353802 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 398ded19-57d4-356e-bd7b-82e2c8cb7ecb | -3.9225 | -55.754299 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d540e60-3037-32b2-a18d-1e9cc375cc74 | -7.6836 | -46.106701 | 2026-09-18 01:02:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cdbc82d-bddb-3cef-9c25-19841dc9d9e7 | -19.556 | -47.639099 | 2026-09-18 01:02:00 | METOP-C | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a32eeda-b61d-3c2b-baab-ebd01718440f | -12.4797 | -50.895302 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74318244-7c42-31c1-9779-207b7244050e | -12.3028 | -50.7584 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ce1e75b-45be-308d-9af8-d2796ff524d1 | -3.2712 | -54.266602 | 2026-09-18 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c211ac-c3f4-3823-a759-d97bfdb3e880 | -12.395 | -50.711399 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d9735104-c944-3c36-93ad-6c5b3f37c06a | -4.5881 | -42.937199 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd1c7aa-d9ee-3d12-9f13-97609380dc84 | -12.2521 | -50.762402 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e617e6a0-97ec-3cda-89b1-10e45dc2864d | -4.3612 | -47.782902 | 2026-09-18 01:02:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 240f8458-750d-3272-9daa-c19529c381bf | -12.4128 | -50.698898 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0fae37-f82c-3173-85c9-65b0a12e0d56 | -11.5204 | -46.873699 | 2026-09-18 01:02:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7d93504-c3c8-3756-ac2d-13ddb0c34719 | -12.3755 | -50.716202 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb1a1d73-f9f5-3923-8685-ceea5e557c93 | -14.6968 | -52.4478 | 2026-09-18 01:02:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab3f501a-e50d-360c-927f-53e750581a01 | -3.9671 | -56.1297 | 2026-09-18 01:02:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a720bf9-dfe6-35f5-892c-f64bd88bebc3 | -16.415899 | -49.962002 | 2026-09-18 01:02:00 | METOP-C | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 729da584-eb96-3d97-abd8-f527bd9df54e | -12.4635 | -50.694901 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f51dba61-b3c7-328a-a999-e1edc37f25a0 | -4.5672 | -42.9757 | 2026-09-18 01:02:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f194da3-0708-308e-9ab8-366b74686a26 | -5.7411 | -57.597 | 2026-09-18 01:02:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63719a04-ea25-30a4-988b-ccf9da86606c | -11.3297 | -43.345901 | 2026-09-18 01:02:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d2375fe-5a14-390b-9fba-9c2f4e159c8c | -15.658 | -52.735199 | 2026-09-18 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b585789c-6748-3a7d-b7f1-ee348b6ddb8c | -12.389 | -50.729301 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 442dfb57-c2de-38c6-9a06-2a7969bf8176 | -13.2537 | -46.8941 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13da903f-20df-3ce7-a913-1a0134fb3fab | -2.826 | -50.497501 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e3616a1-3396-3cbb-8182-ff86b0b4ff19 | -2.9654 | -50.345798 | 2026-09-18 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b2d23f8-2cd9-3d87-866f-aa6080a063da | -5.8944 | -53.518398 | 2026-09-18 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3588bf34-3cb7-3c84-b625-88e27e618a20 | -12.3835 | -50.706001 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e7bec29-0d36-37fa-b48e-05c3a9e43833 | -9.7157 | -54.807598 | 2026-09-18 01:02:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9407d43-8713-3b12-99b2-76b109d5659c | -13.6273 | -46.938202 | 2026-09-18 01:02:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5917e6f-a7ec-3360-91c5-151d5c3dea28 | -6.0135 | -51.771198 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 869b3510-9f13-3031-addc-f3a4e4578632 | -5.7303 | -51.752201 | 2026-09-18 01:02:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 084b0f20-4ee6-3dc5-8618-575a7c021b77 | -12.4146 | -50.706699 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7148a547-3ed0-3793-b21a-948162345685 | -7.0169 | -43.8839 | 2026-09-18 01:02:00 | METOP-C | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 360ae32e-7052-3673-aa8b-dadf3436c855 | -12.2716 | -50.757702 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62168019-9b2c-3592-bc27-700f99eaa419 | -4.7781 | -55.708199 | 2026-09-18 01:02:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1472fe0-7edc-331c-b3a9-629ea2fa5a50 | -9.4005 | -46.8675 | 2026-09-18 01:02:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21bf7779-52d2-3ce9-987b-912ead04f226 | -2.6967 | -57.608299 | 2026-09-18 01:02:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6218c6d2-b845-3c55-9f85-7657ed814b88 | -12.2502 | -50.754601 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9bdbb6f9-d906-3488-af09-da1fd9b60116 | -10.6502 | -50.241501 | 2026-09-18 01:02:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1854c86d-eb38-359c-a2e8-8cfa9183b0a6 | -3.4382 | -58.196999 | 2026-09-18 01:02:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61560720-8683-31d7-ad32-1690928d8468 | -8.5643 | -50.161499 | 2026-09-18 01:02:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 763a0e65-af00-34c0-8334-113cf2e9afaa | -12.3205 | -50.745899 | 2026-09-18 01:02:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ddbf80d6-5da4-3989-bc39-f93fe012b4e0 | -9.944 | -45.346901 | 2026-09-18 01:02:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72f135da-0607-32ed-8613-30abf6a43315 | -9.3934 | -46.839298 | 2026-09-18 01:02:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1627e6bc-6671-364d-934c-d8447cee93d4 | -7.7996 | -44.896702 | 2026-09-18 01:02:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 077c545d-2149-3fa9-90a3-bc0ea3fef579 | -13.2502 | -46.921001 | 2026-09-18 01:02:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README17.md)
