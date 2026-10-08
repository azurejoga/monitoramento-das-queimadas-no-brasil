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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e23fbeb1-39db-35b9-bd18-ece5f1822ee9 | -3.02925 | -53.93046 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4474067f-71f0-3c66-959b-63db5b816a61 | -3.71474 | -59.33846 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a569671a-82eb-3ab9-85e5-bdf6123d2b20 | -3.91745 | -59.10881 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92ae8e57-1674-3947-924e-0620fa95ff23 | -4.36822 | -54.74591 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9806ab8d-8e20-3412-b52a-d355f083ceae | -2.98363 | -54.05957 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c545d12-5481-33c5-bcff-bda4a91bdb4e | -3.24584 | -57.86458 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5709b994-15cc-315c-9a11-c2a78fc9bef5 | -3.67732 | -54.50729 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d51b5ca5-b745-37bc-b9fa-3030c9b4c1b5 | -2.25251 | -51.93424 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8315ad5-9c45-3e97-b411-e3ecfb7fb2a9 | -2.64779 | -56.53747 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fe33c9d-473e-3e2a-a717-52a428205906 | -3.26574 | -54.00918 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3826d0a2-3bea-3e55-9312-fd8221bde2a1 | -6.9459 | -45.27048 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58ff956b-8832-37e2-bd50-9b551e7710c5 | -3.66624 | -57.0918 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb67b810-4223-37ea-b5a5-0b464331d1d9 | -1.82677 | -55.03809 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa8ab022-5c39-3eb9-bf1a-93e74135bdf8 | -3.94985 | -56.04956 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6a76a65-38d3-3b2a-9ed3-b8ba18bd3f8e | -3.00936 | -54.75365 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29a9cc33-0481-3ba0-89d9-0c0b75f877b5 | -3.17591 | -58.6306 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 65326c87-202f-3626-9bca-6f763ebc0309 | -3.86661 | -56.00098 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d522add1-4443-3b0e-9baa-e1f924a0fde0 | -2.46519 | -56.08712 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60f98883-9a88-3840-b6b5-2bc873d62ed8 | -3.98261 | -59.33476 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeb9542e-4ef5-3224-ba5b-8e44fd97269b | -4.12015 | -59.87411 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| edc5a1b2-e661-3814-b1a6-f4fd8d71820c | -2.66274 | -52.57839 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0b47f20-7d36-36d1-a556-466a896bf360 | -3.47718 | -59.58295 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4270fa05-fe4e-3fc6-899d-233483a0854d | -3.21313 | -53.8848 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecee6050-046c-39f1-badb-591484049abb | -3.26825 | -54.68319 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4eec3997-5571-3faf-9510-b5db73e63f3f | -3.05066 | -57.49219 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ec10c6a-6c05-33c7-a2fd-e03c82f1d38d | -3.87761 | -55.82328 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| adcf4151-f253-3bcf-86ae-d82e9e87bcc7 | -1.47562 | -53.61003 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dc43c73-9d35-3934-a0fe-a6151fcb6a4d | -2.46241 | -56.08314 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70a3da89-e039-3fef-8fbe-156fb4b13254 | -2.98266 | -54.11095 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b2e254f-481d-369a-91a7-c967aea8dd46 | -3.74398 | -59.47429 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acc7975a-f9a9-3598-9fa7-f99001ff7cc6 | -3.70288 | -61.32572 | 2026-10-08 05:23:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92dc36b9-4d08-36a9-9cf1-2d483449d1e0 | -3.31079 | -54.04423 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 139283ec-bd83-3dd3-b7de-c3b1117ee31d | -3.67385 | -54.28003 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2e09c49-48a4-39ce-8487-181fdfb2ccd6 | -6.94412 | -45.27613 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d496de56-4ac2-3720-8b6b-cc33af2eb3a8 | -4.26751 | -54.87973 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc72fc34-6f71-32a8-909d-9f6e317d3d09 | -2.49635 | -56.14869 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c88a550-2a3d-37cb-a165-b49fe341893f | -2.37386 | -56.12949 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62d959a2-98ef-3e41-85df-45f1f614f068 | -3.36307 | -54.74728 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab7a70f6-e978-325a-8a76-96cb4c83d65f | -2.76996 | -54.08778 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 728d8e1a-a4b7-37ab-b600-0f5cbdaa323f | -3.56793 | -54.49089 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6ac301c-bd84-38e9-a4ac-f717d7fc78fa | -3.52558 | -54.66916 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa171ffc-80bb-397b-9b8d-f128e1370c77 | -1.34068 | -55.45932 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62638ead-2871-342e-9e97-059dc006d2ae | -10.36644 | -61.22243 | 2026-10-08 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7500d460-6ee9-3c74-ae52-f7458a7abe78 | -3.84433 | -55.99033 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b301fcc-fb1a-3112-9f9a-480e3ad6b770 | -11.97535 | -57.57946 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d782b593-9fa2-3637-807d-48bfa1df7e8f | -3.49578 | -59.26422 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff3242b2-94bc-3d98-80ac-9ca108242a13 | -4.55897 | -54.95436 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84603eef-b5dc-35b8-a464-e7a70f9eb5a3 | -5.81486 | -53.83261 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbc2bc48-161d-3c71-9a73-d21f7617abe0 | -3.55212 | -59.46933 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06f0bd7d-d058-323f-93c3-89e2a12534bb | -3.72275 | -54.22032 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4852554a-89e8-34fe-ba14-3b771d9c4afd | -3.07944 | -54.3945 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f7e16a7-4e12-3c6e-b440-b68848555367 | -6.19284 | -53.15047 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67c3f03d-a619-3f54-bf2e-2c030a2982d5 | -3.32045 | -58.27312 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b44a868-98b8-303f-a125-b658400e3a80 | -3.20013 | -50.55362 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e7feab59-b849-3107-adff-54770f0a3a56 | -3.28076 | -54.05163 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 708561d8-3625-3ef4-9862-0a7d43a5eed2 | -3.55438 | -59.47795 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b57fc47-95e6-3f5b-8691-4d09b59a79a4 | -3.58106 | -54.31749 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5826a373-c098-36d4-b170-bd8957b541c4 | -3.10797 | -54.18826 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aff59fc1-dac9-32e5-9d22-128daa4aacef | -3.10062 | -54.28142 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 415ad6d3-2018-3bbc-a5e6-e38d7a4a64c9 | -7.21777 | -55.12358 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 693bbd2f-8ce3-3b9c-b65f-3e73e903620b | -3.50836 | -54.66645 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28753723-534a-3560-8967-cf380d201c91 | -1.1461 | -54.21905 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aeea2e26-3a5b-3d50-b5fd-f2a7ba602b44 | -6.89796 | -48.71701 | 2026-10-08 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d329432-d765-3d91-90a8-1f993782bf3c | -3.61753 | -55.28116 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12170327-ad72-35e1-93a7-abcc35cce051 | -6.7408 | -55.13575 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ad3e89b-5587-3945-a544-5eb2f04a0f02 | -2.97162 | -51.51101 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc8d2aae-2bcc-3b7f-ba00-fab5b1236fe8 | -2.78974 | -56.49581 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83fe0c0e-ca00-30a9-b47c-2697faa85bcf | -3.18511 | -60.05311 | 2026-10-08 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c17266c4-5a2f-3685-85da-ca868f8494fb | -2.76175 | -54.09437 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 064e295b-9568-3453-a6a2-c079f80d674f | -3.1881 | -60.05805 | 2026-10-08 05:23:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d0e7285-76fd-3a51-9610-ef9bd35335e5 | -8.38323 | -46.30306 | 2026-10-08 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20d82a77-dd0c-306c-95a3-54cf5d34ef83 | -3.01923 | -54.06495 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 811bfc29-fe24-30b0-b686-d46a026a9093 | -3.3083 | -54.69709 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e729a364-d3ec-32d2-ada8-736ae9f99494 | -3.00099 | -54.08988 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cc03795a-8223-3907-86f1-1a29c4594613 | -3.31286 | -54.05139 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 494d261d-210b-3c2d-a061-1e1d988e4806 | -1.45728 | -54.7692 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 452db31a-0490-3373-8def-396f91c7a95f | -3.30893 | -54.05597 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d7b3363-c58b-3aee-8c15-1366829c3bc1 | -3.04936 | -53.91747 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 678293b4-8085-3e80-85b5-3e0121ceba10 | -1.40309 | -54.60638 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c840235-cfb9-3bfe-9b9d-3d0e79d747e5 | -2.91491 | -54.10837 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe05e284-d0b8-3b05-a416-642bee6ad8e3 | -3.11068 | -53.78074 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eeb008f9-2c0b-3a4c-ad32-12844349a4ee | -3.0412 | -53.90003 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53a84849-3370-336c-9465-f59a2bcacc43 | -8.38366 | -46.28687 | 2026-10-08 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89e89902-1715-33fe-bc1b-237ccfe4fa00 | -2.75218 | -54.04153 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f006fbb-8662-327f-86a1-01f4601d8569 | -3.27072 | -54.25216 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fefee68-a31d-3d5a-98d1-833757a282cf | -1.28479 | -54.55869 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c229b827-8118-3558-9d76-a1dc0811f0f7 | -3.51807 | -59.32887 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a2f2e54-331f-3987-82af-efb8f7a074f2 | -2.79953 | -54.08755 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1e75f86-150d-3841-9c6e-67eb904db81d | -8.73398 | -45.15521 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52f5a721-9088-3795-98a8-d26409e74d4b | -2.78342 | -51.68151 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b72b2c7f-7b22-3d59-aa4e-167ac4ac2bcf | -3.0568 | -57.51845 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b23e643-22fe-37d2-95a3-52280163ee36 | -3.07855 | -54.28579 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21e13d69-7257-38ef-aecf-a6f1945589b4 | -2.85664 | -59.11104 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 000d1838-b7e6-3736-8244-1aa7d987d90f | -3.73294 | -59.45191 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b50e8e8-d968-3680-829b-893bfd7b4e7e | -3.0009 | -54.11365 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ac18045-a7ab-3760-ae28-66908731c765 | -2.67078 | -59.91172 | 2026-10-08 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be8b76a9-aab0-3285-9fa0-e36954257907 | -3.57986 | -54.65405 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf495e13-e868-360d-9430-f4d60619de8b | -2.47577 | -56.10649 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 88736067-a65b-3588-a6a5-bf7720720ed1 | -3.68967 | -55.48983 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38e19216-53ef-38df-a420-33fa53380450 | -3.51415 | -54.65207 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README133.md)
