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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2243db4b-2cbc-3c1c-9365-063874022ea4 | -9.7648 | -46.08461 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3096c2cb-89e5-3978-8a64-4ad4383414f9 | -9.92332 | -46.51289 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d613f75-5042-3756-bf54-83654c1b38d3 | -9.7382 | -46.1204 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbe8b855-cd5a-378b-a833-b46f06edfb55 | -10.71252 | -54.01911 | 2026-09-18 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c23997e-1893-336f-b74f-220c20f91560 | -12.56923 | -47.08894 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a75cc3a-933d-3f05-acc6-dcd98820c8bc | -9.76057 | -46.08394 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bc2ca0c0-1123-3dab-994c-a5f1a14bd094 | -10.60079 | -46.54846 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1406eeb4-3d47-33e3-bf4f-63a17dab6c02 | -7.79483 | -44.87754 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a34d15b-f67e-35e0-ac36-850c6214529e | -11.77163 | -47.43445 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf4ea3fd-d739-3994-a5d1-60e13dcf68a8 | -12.4313 | -50.6727 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3bac51e-7634-3ca7-9193-e42b3f7b2499 | -12.17327 | -46.98325 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d00a509-bad3-3010-a86b-63239ccfc386 | -11.32992 | -43.39701 | 2026-09-18 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe21bc46-a296-3e9a-8592-d73ef0893be0 | -11.77393 | -47.43097 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4000a476-f15f-36ed-8b81-79f8343ce8d6 | -7.01348 | -43.63072 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4102981d-b252-3f0e-bb18-834134f353e4 | -7.06013 | -47.47917 | 2026-09-18 04:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6aa5f999-a510-35b6-a273-c1030db827ed | -12.51893 | -47.08759 | 2026-09-18 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ca2d91ce-8fd2-3770-8adb-0c54d0620aa0 | -6.334 | -45.67025 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 118499a7-14c1-3b53-9a54-22a9be470263 | -8.99071 | -50.16738 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3baae94d-6078-38b8-b788-359272dc3e5d | -9.77557 | -45.04033 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 599dadae-1b30-340c-889f-ce4cd4d138a1 | -11.52534 | -46.87604 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a267ffb-24c7-366b-862e-46ae9e5d3d82 | -13.25878 | -46.91359 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1416c1ef-92f4-3364-b432-ed2a1fca7077 | -12.3988 | -50.6791 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3de1a8b8-acdb-3c67-90f4-220f2b854fef | -7.67594 | -46.10615 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9132469f-9a79-3ed8-9260-44acf57e613d | -9.90982 | -46.5487 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee0b11c6-5a2c-318e-9758-71c4d655a13d | -9.19022 | -46.74987 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 505baba6-aa2e-3c61-93f2-e619bab3a72e | -12.20721 | -53.21819 | 2026-09-18 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a20b236-48ee-3f57-9381-721cdd5513a8 | -8.9975 | -50.16842 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4b602f4-cf6c-3259-a998-2ea3c33c6490 | -8.74255 | -45.40925 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae978341-485e-3b07-a79f-49296c016e2e | -10.52123 | -46.72291 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c174e20-ae8d-3495-8901-e2b8ff40ae25 | -8.67621 | -45.31061 | 2026-09-18 04:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1aa0b9b-7925-3c9a-8cdf-265480d3db0a | -12.39035 | -48.46518 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f775477-dbdf-3d22-966e-9a8f090bc7ed | -12.39283 | -48.47499 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4ff43d5b-aa19-39bd-ac9d-9b665027c12d | -12.21113 | -53.21519 | 2026-09-18 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27d91293-74d4-3491-a009-7bbcccdb1adf | -9.15663 | -49.99723 | 2026-09-18 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fa2deead-3372-33f5-9ee1-48f36654e931 | -9.91193 | -46.53378 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c00a2ca5-5702-3047-a661-7ec635e866c3 | -9.94365 | -46.6053 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8486fffa-4311-3854-9adb-ddee1558bfc2 | -12.26025 | -47.13428 | 2026-09-18 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad0ad6ca-9878-3228-9619-2f688cf168c4 | -10.64783 | -50.23027 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e738f12-551d-398b-bcc6-a6184b589985 | -10.65812 | -50.25482 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1e4bb02b-3fd4-31b4-b8df-55040a5d698f | -5.88836 | -52.08719 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3038738f-0667-394a-91aa-bcb0a92faa6d | -10.49117 | -46.29535 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da4b62e0-f324-3a40-8b68-7ffaf5744718 | -8.66006 | -47.46757 | 2026-09-18 04:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 806b0c9d-a85c-3aac-8d66-47218607b748 | -9.93409 | -46.52588 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aadea28c-dc7e-3ba2-87a0-80579b7c87ea | -13.25117 | -46.91008 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 04bd6fa0-d86b-3ea4-8ac7-817615ca3021 | -10.64041 | -50.23294 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bff8f894-923d-32d3-bdb1-3ef24ae6d9c7 | -9.9448 | -45.33778 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976b4e69-4e33-3d8b-9c5e-beb01d3f0192 | -6.93393 | -43.11422 | 2026-09-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62d7017f-f7f0-3eae-a37c-ef9809448738 | -8.68511 | -45.43716 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3bf402c-2355-3922-b40b-0cf0d457e7a9 | -10.68037 | -50.26976 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02e945a9-852b-31e2-80f0-310a30c89bb1 | -7.57903 | -44.91726 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc0ef489-52c6-32b1-a159-c4a9a10dc765 | -9.93825 | -45.31886 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd1afb85-88a7-3a68-bda0-33e58ffa5f81 | -10.61111 | -46.56512 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 42f3a06a-0a3e-3735-8ef3-6a5a4bc93dd7 | -12.47807 | -50.68774 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66057504-4e79-318f-973b-0bae1c8e261b | -7.37333 | -44.46781 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0a6ec826-a320-30c9-a5e3-8a0cbddcfc08 | -7.94909 | -54.88926 | 2026-09-18 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e540499c-e3a3-3927-b732-f0510e3a1ab6 | -6.30529 | -45.69242 | 2026-09-18 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cb1997c-1ae5-3438-893f-e008b5fbfc1d | -8.44972 | -47.65955 | 2026-09-18 04:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c501dc9-e376-309c-a2f1-37864fb98cb2 | -10.66492 | -50.48349 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0a2b9538-b449-34c1-9a53-bb20417bc773 | -12.17144 | -46.98417 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5aba6942-9efe-31b3-9ba7-cb4481b9cddc | -12.39521 | -48.46376 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1133a8c7-c7c1-32d6-9e8a-794dd5e93835 | -9.95236 | -46.60303 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c348693-d592-30a8-bc07-b0a087e696fd | -10.48425 | -46.31405 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 665e3943-7653-3213-b858-2cd562d5b7ce | -9.39136 | -46.8454 | 2026-09-18 04:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f03fce2-365d-3c29-b3cf-870d8a92e7ab | -9.93846 | -53.98738 | 2026-09-18 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca9ddac-3040-3a92-8b79-ff7c2c1d8f64 | -8.51162 | -48.49517 | 2026-09-18 04:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4940864-35db-3854-8eb9-c752cf8eb176 | -9.71172 | -47.09964 | 2026-09-18 04:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b45707fc-489f-34ee-97c4-563488d34a9a | -9.76534 | -46.08075 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab3c604e-db23-3e4e-94c4-b8bbb943c621 | -6.10236 | -57.68721 | 2026-09-18 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6f71b5a-1fd6-33df-9c7c-1490db1a0421 | -7.34858 | -44.64326 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 561510bf-3bc7-3d08-8c79-ac109b729a2d | -12.38214 | -48.46867 | 2026-09-18 04:57:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7dae395f-7025-349c-b147-fc17501a4bf9 | -7.37282 | -44.46957 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8631b67f-2719-315b-9b04-d4393a32a823 | -10.10763 | -45.64919 | 2026-09-18 04:57:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 90876782-8fa0-3a92-8a61-d67c32d36d9f | -13.47107 | -46.90312 | 2026-09-18 04:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ef3455-c83c-3122-b1cc-4a1ddfaa1aa6 | -7.63344 | -46.16682 | 2026-09-18 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8aba387f-1add-35b9-9ed2-56ca540ae4de | -6.03669 | -51.80632 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb25e9e0-ca3a-3001-9c51-5ac09970119f | -10.62844 | -50.24254 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5085c924-0a0f-34e5-a2e2-a65fc43933ad | -8.88387 | -45.88146 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3f5f099-3ce6-3964-84da-fb1ad86c0f46 | -11.5248 | -46.87982 | 2026-09-18 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a4ea766-efda-3423-a581-889fbd641db2 | -7.05814 | -46.22285 | 2026-09-18 04:57:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 016ca8ff-0b6c-38e5-93e9-3218396c7379 | -7.64405 | -44.8144 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ccf6181-7779-3a4d-9086-1553d8e8d77d | -11.87606 | -47.58539 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e07a77b-fb6c-37ef-8867-e876b762cf82 | -8.50802 | -48.49463 | 2026-09-18 04:57:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e8e6afd-1510-36bd-ae7f-36442df3d61d | -6.67006 | -50.90398 | 2026-09-18 04:57:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f01898b5-de71-308f-84dd-edec224a3eaf | -9.75948 | -46.09167 | 2026-09-18 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3736f8db-a3e9-3a60-99e8-1bc4835089a9 | -9.55886 | -45.42012 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0216e464-40a2-3b26-80a7-7a601a9fb5cf | -7.02087 | -44.65754 | 2026-09-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d53d1946-03fe-3c2a-8a03-a751da327bfd | -10.49007 | -46.3032 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4f13f8a-1438-3b13-926d-0aa930c4cadc | -11.89229 | -47.6138 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdd7d309-29d1-35c3-a869-a487879b7b66 | -9.94047 | -45.31684 | 2026-09-18 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90f5dcf0-4969-3e52-a2bd-ac6ae75536c0 | -10.67409 | -50.26496 | 2026-09-18 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 220e1574-e1a6-3b80-ae61-47e2d2649330 | -7.00719 | -43.6404 | 2026-09-18 04:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca59b914-e619-324c-a8e0-8ab2c886068e | -9.93704 | -46.5931 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3af91fb-3c6f-3889-b41a-e0734de65960 | -12.17743 | -46.9836 | 2026-09-18 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aee2be1d-8308-3d31-a2d9-096c767aa4c6 | -12.17781 | -48.97393 | 2026-09-18 04:57:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bcf28eb-e70a-3d45-a187-d0f576bbeddd | -11.87349 | -47.58794 | 2026-09-18 04:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ef532d9-958e-36c7-ad20-9b51ee7664b0 | -10.51714 | -46.72225 | 2026-09-18 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a81a45dc-397c-3019-acc5-e33b911de92e | -8.74315 | -45.40494 | 2026-09-18 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 275a2b57-a9c3-3abc-a6a8-997b1255ac57 | -9.93802 | -46.58628 | 2026-09-18 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cc2ab05-53de-3ec9-941a-726362cdd654 | -7.63956 | -44.8139 | 2026-09-18 04:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c66e82f-419f-32c8-be09-d9e10517e0ee | -12.46803 | -50.88781 | 2026-09-18 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README63.md)
