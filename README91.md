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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1b6bc28-c139-340c-946a-2513363e7fda | -22.49286 | -44.07582 | 2025-10-04 04:17:00 | NOAA-20 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1257466b-d281-35a7-ba71-25c6af39174f | -15.00803 | -50.01193 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35221d85-3f06-3c99-af68-12211473fdfa | -20.12851 | -43.99081 | 2025-10-04 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 47c74b4b-6064-380d-ac92-0f44a1013426 | -21.25736 | -45.18209 | 2025-10-04 04:17:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bbef226f-15ed-37da-a64a-55e4ae4009f0 | -17.30004 | -50.58614 | 2025-10-04 04:17:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa1da7c9-a831-3e92-893b-615d4568ee7f | -15.5992 | -52.46555 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b757f115-8d7c-32f3-8618-6c7af60776aa | -15.59909 | -52.49157 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e215686a-c4bf-3a62-8584-0b60ed3d6bba | -15.58068 | -46.9502 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ae05b0b-7c36-39bf-90b4-1caf2e8e8157 | -17.15092 | -47.03147 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 306053ef-4712-3b8d-9f99-dba4d5f79843 | -14.93578 | -49.96917 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7374a1f5-31c8-329f-8f38-4f21251a83b9 | -15.96148 | -43.33399 | 2025-10-04 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 307f561e-9e6e-362d-8a96-517c74dd6811 | -15.56792 | -46.96375 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66d48183-8895-3926-a3cd-ff8652357522 | -16.76712 | -43.98363 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb2e4000-e509-3db3-a265-8c9da415d60d | -16.39029 | -52.15971 | 2025-10-04 04:17:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1b1b4d4-6d6b-3098-9efa-439e7618eb66 | -16.04 | -50.93878 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b4499de-4183-37aa-aaf3-b4933fd1f29f | -21.68909 | -50.07632 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b5a917ce-8d95-3755-97eb-3ca89ce17efc | -15.52297 | -46.83194 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d553b3a-e57d-3159-b626-5c9079108d4c | -17.29213 | -49.26977 | 2025-10-04 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 038676f1-7e1b-3eb7-9fa1-ccb5e497a97e | -17.29825 | -49.26857 | 2025-10-04 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ad29e1e-444f-3ab0-acdb-847dae888520 | -19.75004 | -46.50116 | 2025-10-04 04:17:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05eb5426-3c4a-3dc5-b891-8e210d024977 | -19.50474 | -43.61376 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2dc863d-6b26-3884-b4a5-faafa4533faf | -17.70283 | -47.08934 | 2025-10-04 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2bf86490-f7a9-38b2-8da7-5a9e968631f0 | -15.60567 | -52.47366 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5acdc43-2dfc-34f4-bfef-d8ad71920fc9 | -15.3816 | -47.96218 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 61b67c7e-7ce8-39ed-b80c-fb39b7137bf7 | -15.53069 | -46.8062 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e124647-f1ac-39d9-90d8-fff782bb5b9a | -20.49274 | -43.78963 | 2025-10-04 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e67dc2c0-cc26-35a4-9275-9b37ce112d7d | -15.26229 | -47.95944 | 2025-10-04 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae0eae60-f00a-3e1f-991a-625a1f6d18cd | -17.69883 | -47.09249 | 2025-10-04 04:17:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3a33be90-f0d6-3ba9-80fd-d112ea06322e | -21.02156 | -45.95238 | 2025-10-04 04:17:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ff4538e0-6a2e-3dd4-b494-8a33772f702e | -15.2405 | -49.30472 | 2025-10-04 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74e6e687-5489-3ef0-aa32-5e3de25a8067 | -16.35045 | -46.98648 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18fdd559-17db-3d9a-b3f3-2272f9560a4f | -15.99829 | -50.92355 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45e4109f-d8a7-3bdc-a525-75de3630ebb6 | -14.98031 | -49.97301 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e299f915-9211-315b-87ce-a8760111051c | -15.52638 | -46.83242 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e881e284-9ca2-35d9-bf8d-75b7affccb4a | -18.3829 | -48.78989 | 2025-10-04 04:17:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 6a8767a2-808d-3ac8-bc30-f872b0df97b7 | -21.12556 | -42.88131 | 2025-10-04 04:17:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8104ac6d-62a8-3cb2-83df-db9fcab4f3df | -17.34079 | -46.83408 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 909e5912-4a85-329e-821e-9c1c235bdb8b | -17.08026 | -46.24087 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34409207-63d0-388c-958b-517fb9625d6b | -18.49316 | -46.09599 | 2025-10-04 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 795ef7f5-8a93-300a-985d-6ff85174c88f | -18.46223 | -49.45044 | 2025-10-04 04:17:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c4d5282-8b1d-37c0-9ddc-90cdd5cfea12 | -14.57713 | -52.49189 | 2025-10-04 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6ef0ddc7-b797-3242-864b-684f88a64842 | -15.03171 | -49.45412 | 2025-10-04 04:17:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 113b721b-25f7-342a-b6a7-381c5da6ad0b | -21.60164 | -45.28595 | 2025-10-04 04:17:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e2713296-6116-322a-b6e6-75e5f2bb0643 | -21.21439 | -45.82572 | 2025-10-04 04:17:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31990d98-313a-30f3-867c-e1f36512db44 | -18.1782 | -53.35985 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9b0141f-a861-38fe-83c4-bbfd61a9fdc3 | -16.00941 | -50.93325 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5b2484a-12a6-3a0a-8185-3f6c84b23a0b | -19.00533 | -47.25702 | 2025-10-04 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ba0f9b04-8c2f-3d00-98ba-3dbdb63bc149 | -15.866 | -46.26506 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14b20fec-bee8-3dd6-922e-25ab86cd15da | -18.17569 | -53.3482 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e0d09238-82f1-3cdf-8569-18b259bd4e32 | -17.247 | -46.80624 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 454e583b-fc54-3c40-90d9-1414024ee004 | -15.206 | -56.83778 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6661b7d1-9161-333a-ac6a-b889fc571d2f | -19.7226 | -47.17215 | 2025-10-04 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0597fca-ab61-3ea5-86c9-ca6b07cb0c3e | -21.18417 | -45.13131 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 54696598-9b9d-315b-acb4-75f6aa965005 | -17.58656 | -44.46338 | 2025-10-04 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51beab44-b58a-3aa1-b833-65187591c968 | -15.9558 | -43.3253 | 2025-10-04 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d72c852e-557e-3200-9066-c475e696313d | -19.57356 | -48.02047 | 2025-10-04 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb2dabfa-316d-34aa-93f3-282a5bde1fe4 | -20.47151 | -44.82072 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e520c7e1-0b02-37b3-83dd-bd825ab0b71e | -20.104 | -44.63255 | 2025-10-04 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 942c1b0e-6ed0-3c62-8178-b999765596b2 | -22.76345 | -45.30622 | 2025-10-04 04:17:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7168e85d-f578-3ef7-91ed-ed7b290ec6e3 | -20.43893 | -44.1642 | 2025-10-04 04:17:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aebc3ace-b70c-3e5d-b554-d701c56b26de | -15.61102 | -46.9363 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d24caadd-306d-3eec-89bb-9750b5415590 | -17.94176 | -47.02349 | 2025-10-04 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3787906f-84a6-367b-831d-63f3f49118d0 | -20.12253 | -44.39153 | 2025-10-04 04:17:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7597e919-a40e-3164-969c-74adc8cfe286 | -18.63997 | -50.67965 | 2025-10-04 04:17:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 73f6488f-5acb-3a7f-a5f1-535f4ddfaaea | -15.23761 | -49.29889 | 2025-10-04 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f95bf642-a52a-3e9a-a46b-6f11cb0a0578 | -15.61719 | -46.94138 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1ea4518-ddcb-3159-874e-7303f49cdb0f | -22.57364 | -42.38054 | 2025-10-04 04:17:00 | NOAA-20 | SILVA JARDIM | RIO DE JANEIRO | Brasil | 3305604 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 21da0490-58f2-35aa-ad8e-61cff3a65ae9 | -15.66223 | -48.14521 | 2025-10-04 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 527fcd2c-d490-396d-ba7c-e73152069252 | -19.68818 | -50.50686 | 2025-10-04 04:17:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eaa19e9-91ef-3cff-99c5-9650687e6046 | -18.27618 | -45.90231 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55e5271f-c325-3ce3-8597-4ea1f9249868 | -15.72716 | -46.2674 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c3b3848-567f-3fe1-a7b2-e11a677cf121 | -21.07214 | -46.90153 | 2025-10-04 04:17:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1638923-38a3-3073-aaac-6291f6a47a68 | -17.26589 | -49.0083 | 2025-10-04 04:17:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49367f76-1375-3f1c-990c-8a3674d89ea7 | -21.15975 | -45.62504 | 2025-10-04 04:17:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f739e90-aadd-3f9f-848d-52f24ddd62bc | -15.71887 | -46.25491 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 29238a1d-11f8-3c2d-afbe-610160327837 | -17.58877 | -44.49396 | 2025-10-04 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e515ef00-1859-30cc-a431-2efac1cf34aa | -22.45495 | -43.18044 | 2025-10-04 04:17:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a58265d1-d0c4-3efa-a478-bd4660c81b04 | -16.01023 | -50.93703 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb01214b-ad83-3cf1-8bfd-713565d668bc | -18.66941 | -43.86358 | 2025-10-04 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 705c3fa9-4be3-3caf-b9bc-9f69b650159f | -14.94708 | -49.97495 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f846d0c-0eea-3aad-9271-3673093e4dc0 | -16.08934 | -51.06919 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8337b68e-5f3f-36d5-8715-f560f6852f65 | -15.99761 | -50.92728 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f70b9fb9-0c12-35a7-bdc3-9518b9b17a58 | -17.15241 | -47.04342 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa6debef-113c-35bc-b007-4a417c663eed | -20.47208 | -44.81691 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eecb73b9-ef54-3364-8268-35bb8a5e67d1 | -15.74332 | -46.26642 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40856018-28ab-33f8-96fb-60e05cf3998e | -19.57693 | -48.02052 | 2025-10-04 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9f8de4d-4cc8-3c9a-9b93-b64f324fba10 | -19.0013 | -43.01731 | 2025-10-04 04:17:00 | NOAA-20 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 36b232bc-ef86-3c6c-a48e-70d244b0be0a | -16.35096 | -47.06806 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 155f6e7b-ffb6-32e0-8e09-d34d1e579e5b | -15.90378 | -47.94444 | 2025-10-04 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dba7c32c-0e65-3828-b717-8299e3619d13 | -19.96565 | -43.64121 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1d5969e4-2671-3c3f-a1b2-c6bd3b00d733 | -17.55997 | -46.76131 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 635aeb38-9cd9-3f05-8412-93f61a7a3b2d | -16.08445 | -51.07225 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 154085e9-7ad0-399c-8ae1-9211ad242117 | -15.8666 | -46.26136 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56644391-3920-381f-8800-7dac101840dc | -17.55148 | -44.42313 | 2025-10-04 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ab8e4b2-9c1c-382f-be56-4ea2b1643f1c | -18.54822 | -45.04935 | 2025-10-04 04:17:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37aba13a-98c2-37fe-830c-a789f2eb37c4 | -22.28309 | -46.74411 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c674501-0668-37af-98a6-7766a93e633e | -18.38645 | -48.7906 | 2025-10-04 04:17:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 29782688-8ab9-36ea-8c02-a2c7452c9bf8 | -18.23501 | -53.36717 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0e10b0f-2adb-343e-bf0f-11ad1da5c2ab | -19.71397 | -44.12816 | 2025-10-04 04:17:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7eee8f3-0879-315d-bd6b-0d74a03ed7ef | -16.02615 | -50.94385 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README92.md)
