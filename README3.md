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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1479cd67-fac6-3525-92eb-3d868cd61395 | -5.705 | -53.441299 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4950832-5af1-345c-bb64-83d765696f85 | -5.996 | -40.9795 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ad3e481-e0ef-3a42-86d6-a1d9bff3b1e3 | -11.9079 | -46.556198 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce191d0b-963b-3fef-b9de-5f2d997ec48a | -15.7977 | -50.123798 | 2026-10-09 00:06:00 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 44c6a341-9054-3b96-b39d-5e188bd6e431 | -5.3732 | -48.9813 | 2026-10-09 00:06:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 049c498e-046a-3de1-9bbd-764ef7fef925 | -8.9022 | -44.941299 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7f3c786-2fb8-31ce-bbd9-212f4804de77 | -6.5126 | -45.402 | 2026-10-09 00:06:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 790000f7-c729-379a-a578-ddc215e912b5 | -3.0335 | -54.2631 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67361a7b-f847-373e-bdb8-bb84e9bd1e2a | -2.9873 | -48.916801 | 2026-10-09 00:06:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd1f156-7eed-377c-a4c1-ac249a2b2f0e | -4.0773 | -44.109402 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58086fdb-6c2d-3ac4-8b6f-f94bdf45ea0a | -5.7469 | -43.285099 | 2026-10-09 00:06:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b1b10e0-fa10-34a8-9c1c-155816d9d51a | -5.7484 | -43.8577 | 2026-10-09 00:06:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1475d6-9ee6-3e40-bffa-0c979124dc77 | -10.9087 | -50.749599 | 2026-10-09 00:06:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 037fdf0d-bc9b-3209-b7a1-5989a87e2884 | -6.3302 | -43.355499 | 2026-10-09 00:06:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c741c39-59e9-379c-bfd7-df868a64d3e1 | -5.2947 | -47.908199 | 2026-10-09 00:06:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8b4b14b-20cf-3b1c-918c-92ca7ba39147 | -17.9547 | -43.266201 | 2026-10-09 00:06:00 | METOP-B | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 68a168ac-b3c8-3d0c-b4e7-20754bbb0540 | -14.9968 | -44.057701 | 2026-10-09 00:06:00 | METOP-B | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e25b1884-0a77-309e-b993-41d5123702a9 | -2.9933 | -53.851101 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fbd52e8-1c85-3536-a70d-f5dfaadb8c34 | -2.3242 | -48.493401 | 2026-10-09 00:06:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c4bb689-8ac5-31fb-8da1-53e78f36f0d4 | -3.4674 | -59.481499 | 2026-10-09 00:06:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd3e280-8d5f-3e53-acb3-c47f5b3d0992 | -7.2359 | -55.134998 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f69f77ad-a89b-3e72-add3-78534698d908 | -6.7228 | -55.122501 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 684b77ea-1a72-33fb-9882-fdae82b88064 | -3.1109 | -54.194901 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 547b194e-125d-375c-89cd-d39267267dae | -5.7113 | -53.4701 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbf5c4ff-f217-3055-9b0f-af17adb89f4b | -11.6501 | -43.675999 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cdaf4988-ba2b-31b4-b0aa-375339131831 | -7.2249 | -55.0835 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d721799-cbb5-3e37-83cd-bb4cc18dfe53 | -6.8872 | -45.903999 | 2026-10-09 00:06:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6959cc8-fe08-3f76-b828-ca3be43546e9 | -2.8781 | -54.1642 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e37fab31-8f66-3ed7-84ee-25d68b5934d4 | -3.2626 | -53.999901 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6183217-9f9c-3c86-994b-6040ab7031bb | -5.5951 | -47.2812 | 2026-10-09 00:06:00 | METOP-B | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50eb1760-acce-38d4-bc1f-d1e510c53535 | -8.321 | -49.1222 | 2026-10-09 00:06:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6bcc3e9-d209-352e-b966-498e353c8581 | -2.95 | -54.118198 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d6f1397-d1f2-312f-8829-a8a16bb4359d | -2.9317 | -54.081902 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 706fea9c-d16d-3fd0-a907-fffaeb9186ec | -9.2738 | -47.447201 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9606c828-1150-3e91-b2fc-cc83283340d2 | -5.094 | -46.222801 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a5eb03d-9829-3b9b-9630-8939646c0c77 | -3.0066 | -54.095699 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d13e4558-ef6b-301b-b139-a0c5eff9aa4c | -3.0318 | -54.070099 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dd8977e-700e-3183-b3d1-209677b87bde | -15.0935 | -42.002102 | 2026-10-09 00:06:00 | METOP-B | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0ef79f1c-6714-30e0-bae1-4af1f729850e | -8.218 | -46.438702 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79d96e30-10f0-3b25-81cc-1df6cf36bc21 | -5.3812 | -44.223801 | 2026-10-09 00:06:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57063a5d-6548-377b-85a0-e641eb683b9e | -11.0008 | -47.4697 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac07b2ad-c0ce-31a9-b325-362c04174f97 | -4.3274 | -55.015499 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d72873e9-276c-3ad7-b4fb-e5306d098c41 | -2.9772 | -54.1021 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60acb539-125e-3530-8adc-97819efae468 | -3.2015 | -50.5495 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 865e2874-6eb4-35b2-98d4-2103de8c7f5e | -14.7821 | -42.8937 | 2026-10-09 00:06:00 | METOP-B | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 405a500d-12f8-3365-91c8-bd336dba1c49 | -12.2161 | -57.1036 | 2026-10-09 00:06:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca9f3399-dfd8-3252-821e-7dd7cc8b975c | -13.1458 | -54.3293 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3385917d-6280-374f-b348-b77410036051 | -4.9268 | -45.723 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a75dd16d-cacd-3834-8b8b-1ff21b4d41ce | -4.9852 | -45.3083 | 2026-10-09 00:06:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31125f5e-ce99-33e3-aa06-5e7f0c4e6e0e | -16.523199 | -42.516399 | 2026-10-09 00:06:00 | METOP-B | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c2039073-d378-38c0-8056-f7cbb0ca1e6e | -11.6199 | -43.722698 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75640cfe-42b1-33f5-84d4-29039cc91b2d | -18.5825 | -41.483299 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DE MINAS | MINAS GERAIS | Brasil | 3161056 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbe4a8dd-3847-3701-b5b3-13e265600150 | -1.1014 | -54.168999 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71924709-6789-37e0-b086-ceacf5e36f9c | -13.4824 | -42.482399 | 2026-10-09 00:06:00 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f65c3b69-17a2-3673-b458-1f00ad0cf845 | -14.8716 | -50.297501 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ebac8851-6340-3e9c-8eea-41b00233b854 | -4.5498 | -47.040501 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99ec860b-e96f-3d2f-a1fb-8f00ef1bb283 | -11.9692 | -57.604198 | 2026-10-09 00:06:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7245ce2c-5c74-306e-8bef-b0cc32a4f400 | -3.2456 | -54.663898 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c0b48a8-e6f1-3d19-98f6-4189d79d8047 | -1.7381 | -52.241402 | 2026-10-09 00:06:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e2fe180-86bf-3be7-8314-aa85a4307b00 | -6.9402 | -43.666901 | 2026-10-09 00:06:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9790606d-1e55-3c3b-aa1d-23631dfd3d5f | -6.4989 | -55.3167 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1adf45e-cf31-3796-847a-5ca6397951b8 | -3.1239 | -54.1614 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d7fb716-0446-37cd-b001-750f29f37004 | -2.0713 | -46.57 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3a2661e-5a9a-36c7-87d6-0254076c3d69 | -11.8342 | -43.581402 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 292e32af-1b28-3ddd-ab56-da9c81b45fce | -3.8296 | -55.965801 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f77f7e65-e892-37c2-befc-74da0590a777 | -5.3164 | -43.424 | 2026-10-09 00:06:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df8f18aa-2132-3c6f-8968-26c10fa3668f | -8.597 | -49.529499 | 2026-10-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b6d32ba-8741-37a5-b794-534eca6743d8 | -6.7255 | -55.135101 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 946273fc-9cb2-31d7-a6d1-709cde900414 | -1.5461 | -54.5471 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac7b1a28-8101-3c61-b4a3-fd13febf07ad | -16.9307 | -42.1036 | 2026-10-09 00:06:00 | METOP-B | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba665e18-5cab-3401-b87c-782b0bba1330 | -14.4281 | -43.925598 | 2026-10-09 00:06:00 | METOP-B | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc7a277-66a4-3d03-ac28-584e7f8dd905 | -2.9956 | -54.1385 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b752f69-87bb-3a5c-91fe-4159b5fce152 | -11.764 | -45.4795 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cfd17ef1-bafd-32f7-809d-4ab194d26560 | -10.4589 | -47.856201 | 2026-10-09 00:06:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9bc6c49-8915-357e-b8ed-f4434cfe5b4a | -8.3195 | -49.115299 | 2026-10-09 00:06:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc691949-9445-30e4-9d07-0adc5e04b6db | -3.2154 | -54.296101 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e6b89e-10ed-3cd3-92b8-483cea831b3d | -9.6267 | -48.881001 | 2026-10-09 00:06:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c41faf81-8145-3868-b5ca-2f514c9b026f | -2.9968 | -54.097801 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 538139d3-3fad-35dc-8e8f-f9ac4058a9c5 | -18.2922 | -49.5177 | 2026-10-09 00:06:00 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed4d2379-ca20-353e-9742-48c986e058f2 | -15.9539 | -40.832802 | 2026-10-09 00:06:00 | METOP-B | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37bd8b65-435a-33fc-bbeb-6cb11b71c679 | -14.0461 | -43.840199 | 2026-10-09 00:06:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9e13f3-39e4-368f-b838-0c2e72c87253 | -9.8545 | -47.4613 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c5eebfc-9ccb-37da-bf1e-9793aa02e63c | -2.9926 | -54.078701 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7fac851-a78a-3810-a26d-7b2902a0fd08 | -11.7118 | -43.631302 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef46e70d-ccef-3047-bdc0-85159c016bbb | -8.0737 | -45.636501 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63abd646-7231-3965-b533-9679000e5462 | -11.1868 | -45.306 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07e2565f-e1f1-30fe-979b-f284c5c97411 | -3.7734 | -58.555801 | 2026-10-09 00:06:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7a6083-5458-3723-8b70-4e8f85ec06f5 | -3.5438 | -54.6213 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1739597-4040-315b-ba33-9fe6bcd32564 | -2.5007 | -56.0648 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40c6e31d-1ab2-3a88-a91b-b21acc780068 | -3.1819 | -58.6409 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d715326-a53a-364b-a1be-56101deb2c23 | -5.615 | -44.385399 | 2026-10-09 00:06:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eee641cc-6cbe-3034-b33a-6f45e624a3fe | -8.9713 | -45.902401 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49501c11-9e98-3779-b084-799d33c6f010 | -7.2575 | -48.059399 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5f9b1fa-79de-3f73-96ba-0b182d276fa9 | -11.7667 | -44.957802 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9137dc0a-a93a-39aa-bb00-d9973c657421 | -3.5849 | -54.667702 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06f68f60-b70b-3fb9-b76a-262f340488cb | -4.6666 | -56.195499 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac18eba8-a05d-3911-b43d-271ea7a64e88 | -8.2338 | -54.739899 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22b6970a-c260-3c36-8f15-7c913ee7349b | -6.7326 | -55.120399 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92fbd589-564d-3943-a9dc-60b3210860c5 | -6.4491 | -55.036301 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adc3784a-347f-3737-bc5f-93dc5923597c | -11.6448 | -43.696999 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
