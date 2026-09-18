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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88b23a14-454a-3460-ad28-e9815b1e4e79 | -3.7042 | -60.621498 | 2026-09-18 00:39:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fc560fc-130f-35b0-97bc-71d76e41facb | -13.3882 | -57.024101 | 2026-09-18 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d92f782c-5c8a-3c37-a7db-e0d827a49c92 | -16.329201 | -58.124001 | 2026-09-18 00:39:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ba0457d-b78f-3ad0-bd83-7da66cb7e649 | -12.6274 | -50.9002 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d439fae-ff17-3344-b001-200a97e22f4b | -12.4554 | -50.703701 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 459abe26-4ed8-307e-8671-b85a9eae4714 | -15.8042 | -52.5569 | 2026-09-18 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1abaece8-4bdb-380e-ba51-675d3b00bb95 | -3.4258 | -58.188801 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45c1301b-a8dc-3a38-a18b-bbb496dc48c8 | -12.4057 | -50.669601 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bad7f263-7aa0-34f9-b169-0c3dd4771528 | -5.9771 | -55.356098 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76e3d8c4-42ac-33ab-888b-b92fe4f3e7e7 | -12.6494 | -50.905899 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d35c9506-bb19-3d11-95d9-759d188a6837 | -12.2633 | -50.763802 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d62304f6-a105-34e5-8198-0971f1ccf282 | -10.6142 | -46.5564 | 2026-09-18 00:39:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 660e6455-b7f8-34b2-a335-5384443bd93f | -8.9238 | -62.4245 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 324bb012-9cb0-3aa1-8e76-1e382f9cd120 | -4.5227 | -56.073502 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0eef165-ea1d-3f9d-82db-05ada746fabc | -3.6031 | -59.066799 | 2026-09-18 00:39:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72f268c5-2a1d-307c-8923-954c70a36fde | -3.9686 | -56.129799 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70e3055c-a5be-3473-a768-88aadf4bb7f5 | -19.5446 | -47.617599 | 2026-09-18 00:39:00 | METOP-B | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| eabf173b-33bd-3f35-b90a-68290c8207f5 | -17.773399 | -46.487499 | 2026-09-18 00:39:00 | METOP-B | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7171f2a9-d6f6-3db5-b82c-274475dd9436 | -8.8726 | -62.423302 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 052e69cd-c937-37da-b66c-636f3f806ef0 | -8.8628 | -62.4254 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6fdd693a-6507-3a8e-a0d1-4a07edd156dd | -7.6618 | -46.098999 | 2026-09-18 00:39:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d05e4111-4b07-3d2c-a4af-41f58d76e9f4 | -7.1088 | -55.120499 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c87bf692-bb96-3ecc-8d57-4260255d62f6 | -5.7536 | -57.591202 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769ba223-e083-31a8-9a88-ac3975e00080 | -3.7059 | -60.629299 | 2026-09-18 00:39:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff76e25f-4aa5-3bfe-8730-3cc053b9ae90 | -11.0226 | -54.1534 | 2026-09-18 00:39:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b55aca2-34f0-3e56-855c-e511a9fc2c26 | -10.6539 | -50.4767 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd61c877-6d17-32be-94c1-a794bc40097c | -12.2068 | -53.2085 | 2026-09-18 00:39:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9637ddb-e476-337a-b145-6e55b5fab076 | -10.9971 | -57.047401 | 2026-09-18 00:39:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37259c88-83ba-3de6-acf8-07f830878b2c | -4.5402 | -54.936401 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 939cce35-1683-350d-846a-7d0bee184ab8 | 4.112 | -60.904999 | 2026-09-18 00:39:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4c598d6c-a2fb-3118-a1a7-834bc8257d86 | -4.3711 | -55.411201 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e906da85-b0ec-332b-a202-b0be5d5ad25a | -4.5659 | -54.9137 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eac760c-dbaa-3d2b-b7ba-c5c388ba12dd | -13.2487 | -46.887901 | 2026-09-18 00:39:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b837d0e5-6d7a-382e-ba03-b2aedcc0a2a6 | -3.4808 | -54.7211 | 2026-09-18 00:39:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 411fbcb0-acb4-3e31-b324-5f53b67e099f | -11.298 | -43.420502 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 862b7d77-199c-36e8-8461-a7b81fb1ada3 | -11.1359 | -49.045399 | 2026-09-18 00:39:00 | METOP-B | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a86653a-f6f3-3e2b-b915-84e98f8d5ac6 | -2.4896 | -49.4123 | 2026-09-18 00:39:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9c443cf-8165-3401-993d-e55cb29cb567 | -3.2616 | -54.261398 | 2026-09-18 00:39:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 434614e6-4484-3bf0-8996-9d602a0b5335 | -12.2828 | -50.7589 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7c651dea-39c8-33bb-9606-c9034fb746ae | -12.3368 | -50.768398 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 929f7488-94a6-3153-a4a5-103693408f1d | -3.4789 | -54.7127 | 2026-09-18 00:39:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88199353-6579-36d7-a394-d84260941405 | -8.897 | -62.3941 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e73e3bdb-b8a4-3e8e-9c93-1314b70678bf | -12.3943 | -50.7075 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5546309-e7c5-39cf-9b81-4296b2b06524 | -3.9216 | -55.744301 | 2026-09-18 00:39:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef417a35-6521-3562-b524-ef6d0e0a6a7f | -13.244 | -46.909401 | 2026-09-18 00:39:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c0b2f6ad-2956-3b9a-9d47-683ed7fdfa27 | -12.4657 | -50.873402 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 569b7eaa-8db2-31a3-acdf-40aa3c9938a4 | -12.3288 | -50.735699 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad8242c1-c348-3170-860d-66f6a0dbb0e5 | -5.7383 | -52.25 | 2026-09-18 00:39:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81c9b17e-0eec-364c-b89b-9aabbc27147b | -3.3028 | -57.872398 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96f3b344-a3e9-3c50-9b33-4deeb8b7f79b | -3.722 | -60.609402 | 2026-09-18 00:39:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4435f7e5-c890-3ade-b8d4-808218586c3d | -4.3554 | -47.770901 | 2026-09-18 00:39:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d127b782-d1ee-3582-bf17-3a9f759bf733 | -19.1817 | -48.760201 | 2026-09-18 00:39:00 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 16f56471-a4aa-3482-a7d1-26b9d57f757d | -12.6442 | -50.884701 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e253836-b429-339b-8bcd-228e69c2308c | -29.347601 | -52.4883 | 2026-09-18 00:39:00 | METOP-B | SINIMBU | RIO GRANDE DO SUL | Brasil | 4320677 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 618ab1bc-f772-3491-bcc0-3e7ec8be9886 | -12.4111 | -50.691601 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e716a41-aae6-37e3-871e-7cd5b1e2703f | -4.361 | -47.793999 | 2026-09-18 00:39:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d68764b-5d3f-359b-9c06-dd13ac072758 | -2.8113 | -50.473598 | 2026-09-18 00:39:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b10f986c-f9ec-3545-8eda-fb0e714505bb | -3.4483 | -57.969002 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c3a5066-6f2d-3831-8a81-f3eb5c7060cf | -10.6763 | -50.483799 | 2026-09-18 00:39:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbb5e624-d7f2-3fab-a2e2-ec2fc691ce6a | -10.892 | -53.990299 | 2026-09-18 00:39:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20905497-4ccd-3c79-b6a6-85bfcdcc53bd | -14.7042 | -52.4496 | 2026-09-18 00:39:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb97504-0cce-3082-b383-0d152f9836c9 | -11.0624 | -48.302898 | 2026-09-18 00:39:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4aca585-c089-3cdd-a62d-f59e2c48fe97 | -4.5085 | -54.9772 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c2539e2-fc7a-3bad-ae59-6b7683361a2f | -2.8915 | -54.174801 | 2026-09-18 00:39:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 478c8792-d7ac-3ca9-86f2-3f8da523bd3c | -6.3631 | -58.287399 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78ed4cf8-be2e-372d-b680-86f0eb2f00e7 | -12.3819 | -50.699001 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa66e16a-46a8-3c5c-9765-ab3f8d3aebe6 | -12.3987 | -50.682999 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8309c44b-d52b-3295-8d84-220a18c0e3f5 | -8.9068 | -62.392101 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e007db3e-7b21-3e6f-bbba-b415867b9c6b | -13.2633 | -46.904099 | 2026-09-18 00:39:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcbfbad8-8371-38d4-8922-091b29a49dd5 | -15.8548 | -57.5667 | 2026-09-18 00:39:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2754f98f-c5e8-34bb-89f0-a15e9a50526c | -13.7217 | -51.664398 | 2026-09-18 00:39:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ddabdd00-898a-37e1-aa9f-aff46de8a0db | -12.3315 | -50.746601 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32c0d8fa-6adf-357c-a173-15f57a4dde9f | -11.2789 | -43.388401 | 2026-09-18 00:39:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bcc83bef-626d-3ee7-af8a-551b110e57b7 | -3.4385 | -57.9711 | 2026-09-18 00:39:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16e77e76-6d6d-3359-81d9-727ec0f1845b | -4.5384 | -54.928398 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3804151e-7e2c-3701-9904-3194d85302f5 | -5.9006 | -53.5116 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17b16bfd-0ab5-3043-8c5c-407a8c88d967 | -3.447 | -58.191299 | 2026-09-18 00:39:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0981a1b1-f30f-3687-ac55-27552d444057 | -4.4754 | -54.967999 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f80ee8cc-dc2b-3eae-884b-4409f79a12b8 | -12.4695 | -50.6768 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 858bbcaa-c96a-3a0c-a218-af14a641b931 | -5.6641 | -60.2341 | 2026-09-18 00:39:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1333992d-3880-3ef7-b2e3-6d2c58dbbba0 | -2.6961 | -57.605301 | 2026-09-18 00:39:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30b79074-6472-3ccf-b649-7e7a611397c1 | -14.8977 | -48.141602 | 2026-09-18 00:39:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e6670a15-d13a-3d78-8ace-d21b76872dd1 | -9.1539 | -49.998199 | 2026-09-18 00:39:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f24d0641-3bb0-3ca4-ade2-833812a37a9b | -12.6345 | -50.887199 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2292c464-cd1f-3432-b74a-ba926b7c2e8c | -16.327499 | -58.115601 | 2026-09-18 00:39:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6992a0a8-bb78-36c5-b090-bb979f8a637f | -9.38 | -46.8368 | 2026-09-18 00:39:00 | METOP-B | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45c51e26-b431-31ef-b533-3bd8182f0539 | -3.7283 | -60.591702 | 2026-09-18 00:39:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08bed0ed-a967-353b-9e1a-83ea53ae3bdd | -4.5365 | -54.920399 | 2026-09-18 00:39:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8e2c2ae-0eb0-37cd-b6ee-d2259ef69f1a | -12.404 | -50.705002 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d5d234e-71fd-38ae-84d0-ba12fe080f9b | -6.8709 | -53.4282 | 2026-09-18 00:39:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 672588b9-bba2-378b-b6cc-f955e49d7595 | -4.5146 | -56.083 | 2026-09-18 00:39:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9e5a60f-7b76-33fb-9825-0d32dfaea264 | -8.8701 | -62.4118 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf271bb0-5cce-3e79-9255-8c63980151ce | -5.1766 | -56.182999 | 2026-09-18 00:39:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8aaec56-28e4-3dc8-bf2c-d9257acb6893 | -3.3395 | -53.262501 | 2026-09-18 00:39:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4974ecb2-78f2-32b0-b8bf-929ceb2daf83 | -5.7407 | -57.5797 | 2026-09-18 00:39:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 110e15d5-aa82-39b1-9a93-3308ad534d78 | -8.875 | -62.434799 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9e74c3-3c5a-32ba-80c9-274ba0be16e0 | -14.7023 | -52.441299 | 2026-09-18 00:39:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 181938ae-db13-38a5-905d-1860c198c2ff | -15.6583 | -52.7286 | 2026-09-18 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 166f5896-9715-366b-b543-9c14a4409f93 | -12.4403 | -50.684101 | 2026-09-18 00:39:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| addc7291-94e4-36cb-b36f-9708b310b539 | -8.8774 | -62.398201 | 2026-09-18 00:39:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
