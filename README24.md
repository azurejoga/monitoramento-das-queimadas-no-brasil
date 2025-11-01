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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc48f4e9-9b60-3df9-9a40-4253339c1aae | -13.87431 | -56.33667 | 2025-11-01 04:40:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42631334-cae0-331c-979c-f3a6353bf358 | -10.15387 | -43.92262 | 2025-11-01 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3e1e20d-c0e9-39f2-860f-b7cde445e062 | -14.97962 | -43.55744 | 2025-11-01 04:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 36f2cb07-6019-3d56-af8a-a3b6015634f4 | -12.9118 | -45.06375 | 2025-11-01 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9852de6-63f3-35f3-9767-a03a21cc628d | -13.75175 | -43.60128 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fb61384-2241-3b30-b9dd-f03731abd212 | -14.58716 | -44.76918 | 2025-11-01 04:40:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45052e70-f17f-32a0-8e8f-05cebf2299e0 | -13.3832 | -54.293 | 2025-11-01 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c31f7a-c2df-30ac-ac86-ccd3494e533a | -9.57202 | -50.89075 | 2025-11-01 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d549439-c30d-305d-b27a-76a8768b5c6e | -13.03038 | -48.25396 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7af0e8c6-adca-337b-b872-f03d384ab51a | -16.3168 | -50.04804 | 2025-11-01 04:40:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38983029-f9ce-3a58-bdd4-bbc282b13763 | -10.24093 | -44.55415 | 2025-11-01 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47e30169-e525-3efe-bbcb-408bdef4077f | -12.53606 | -48.71231 | 2025-11-01 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8fdffba-7304-360a-a51f-2dd08f453844 | -13.14317 | -48.46899 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35cbfcec-5d3c-311c-b417-ab6ffc7f484f | -10.42581 | -49.37195 | 2025-11-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 100d8c93-a035-3359-a911-a4c3caae2b49 | -13.71598 | -43.78284 | 2025-11-01 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 235b1873-f47a-3b53-9b1e-644ff0a76e88 | -14.02778 | -43.41232 | 2025-11-01 04:40:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de0f768e-0942-371c-a63b-48b73300bf6d | -15.5567 | -51.49918 | 2025-11-01 04:40:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5ebccd9-89b8-34a7-ba69-355701c3a616 | -11.18479 | -47.83537 | 2025-11-01 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4eb4dbd9-9c1c-346a-949c-6530588fbfbe | -13.84529 | -47.06168 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f41176-bc53-3d15-a5fc-784b6fb71706 | -13.14552 | -48.45296 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d6c7f06-6a94-3554-981e-de45ef510a4d | -13.97508 | -49.23772 | 2025-11-01 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd3021d1-2825-320e-9d79-32e4a6255e4e | -10.15234 | -43.92347 | 2025-11-01 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2a4c26e-1f68-35b4-8209-d0dbef4e4ba8 | -10.63769 | -52.18759 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef2cab7a-19b7-3983-a0a6-403a10c4b017 | -13.19791 | -48.31511 | 2025-11-01 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 731d149c-3cdc-3ae9-b11b-b4a19bbcbe35 | -13.84842 | -47.06669 | 2025-11-01 04:40:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 637420d2-11c8-3464-806d-4dc9dabba15f | -11.46689 | -49.80759 | 2025-11-01 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2913be5-14f5-318c-bcff-f1e25663348b | -11.38449 | -48.92947 | 2025-11-01 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 72fe25a2-eb0b-3f80-9028-92a53a279a81 | -12.90853 | -45.0656 | 2025-11-01 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d7c9d6f-0eaa-3465-94fb-89a553c41114 | -15.56085 | -51.49612 | 2025-11-01 04:40:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3437fe33-5824-3c05-aa34-8bc22df31ac7 | -10.63367 | -52.19078 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb586358-ab28-387b-b199-8fb6c9e9cc09 | -10.7935 | -48.45871 | 2025-11-01 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8a15bda-aa9e-3b6b-a4d1-993808a33461 | -15.56029 | -51.49969 | 2025-11-01 04:40:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69b940d9-2274-3ad5-bce5-4c1bd9559688 | -11.73904 | -59.30933 | 2025-11-01 04:40:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb7800df-689b-396c-a46a-4b788f4edd01 | -8.63074 | -54.8944 | 2025-11-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a381995-da75-34fb-a79b-2df0cd586852 | -10.33937 | -44.65253 | 2025-11-01 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e09deec-757e-377b-a4e1-ce82ffa5c434 | -13.01034 | -43.85564 | 2025-11-01 04:40:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 088e2737-6e6d-36e1-8993-73500151e345 | -10.63205 | -42.31261 | 2025-11-01 04:40:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f009d62e-4f19-3f2b-94fe-ad01a1907972 | -11.27833 | -41.73706 | 2025-11-01 04:40:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7ea0047-77ad-30b5-87ee-0cdaa2edc7ef | -9.90913 | -50.50311 | 2025-11-01 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8fb488a-a210-3eb5-ad2f-b6863ae9f794 | -14.02617 | -43.26647 | 2025-11-01 04:40:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63d90fa1-92f4-3078-8373-5279ce07ece2 | -10.62806 | -52.18214 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 91475b5b-581c-3a98-92e9-7c5c108c732f | -10.62745 | -52.18589 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92789d35-945d-3a48-b305-54e1426159fb | -13.41189 | -42.99097 | 2025-11-01 04:40:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 37bdfd20-7380-3d9d-88db-fb6579f35401 | -12.30088 | -48.04834 | 2025-11-01 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fcb13504-d47a-3ca6-8143-2226682705fd | -10.63428 | -52.18702 | 2025-11-01 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5bb6b299-9d6f-3da9-b638-85c37e76346e | -17.8215 | -54.89943 | 2025-11-01 04:42:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39a764a1-c61e-390f-b0d7-688240e19155 | -21.16509 | -57.4276 | 2025-11-01 04:42:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 974fdeae-0430-3f86-9023-a2ce36f9814a | -17.9582 | -52.68649 | 2025-11-01 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a101d859-fbe8-3e3d-aa54-ad80a3fbce0b | -21.77148 | -55.95715 | 2025-11-01 04:42:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83bc883f-6fc2-3c82-9322-7b7745ec4601 | -19.48007 | -54.80847 | 2025-11-01 04:42:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60660418-b473-34e2-8e1a-9ca32e2b09e1 | -21.76945 | -55.94778 | 2025-11-01 04:42:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85be7915-8e2c-3d0c-917a-58afe7e00460 | -16.24164 | -55.72776 | 2025-11-01 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 208c4126-e3f3-3a0f-b3ba-d788fd8ee591 | -18.90239 | -47.50907 | 2025-11-01 04:42:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 236212f5-2814-3e25-8636-4268c27e4b2e | -17.96152 | -52.68708 | 2025-11-01 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e292bd21-55ba-387a-b81a-2cc82a16e1fa | -17.82504 | -54.90009 | 2025-11-01 04:42:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff04e087-156f-3c1e-99fc-7e99af5fabd1 | -26.4783 | -52.02699 | 2025-11-01 04:44:00 | NOAA-21 | PALMAS | PARANÁ | Brasil | 4117602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 888964e0-baef-3214-9c38-b2dd3a692550 | -25.46546 | -52.90614 | 2025-11-01 04:44:00 | NOAA-21 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e2cfad10-3fcd-3aa1-bdf5-101c52c2e902 | -3.234 | -50.5789 | 2025-11-01 04:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 94b74040-cb0a-3a56-b5d6-402ba11d0f91 | -3.234 | -50.5789 | 2025-11-01 05:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e1697026-d596-3910-972a-69e57587b305 | -10.6313 | -52.1891 | 2025-11-01 05:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0d55bb1a-2ada-3aa4-8ce2-cefa09b9de4e | -10.4219 | -44.3542 | 2025-11-01 05:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 139a4344-5450-31ef-955e-bde604d17962 | -3.23598 | -50.58423 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f28e00a7-f1fc-3044-9f37-66ae97a1cd74 | -1.78058 | -55.53442 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdb551ad-8444-3f1c-8c6c-a228cff79447 | -3.03828 | -45.8221 | 2025-11-01 05:06:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66b067c8-2e85-3ede-8b7c-2618395227c3 | -3.22347 | -50.58736 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4071f6e8-083d-30ba-8a71-2cd49f166010 | -1.8207 | -55.35943 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe0cb4c9-06f1-3b72-babd-6921e8fdad5d | -2.53014 | -45.84803 | 2025-11-01 05:06:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e55acbb-4c74-3c5e-a50d-686df6db905f | -3.77294 | -47.62358 | 2025-11-01 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca8a1d53-c752-3459-b4a8-8973dd68810e | 0.67947 | -56.87044 | 2025-11-01 05:06:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c1fe886-b5b1-325b-943e-05d1a7732ff9 | 2.12577 | -50.97975 | 2025-11-01 05:06:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5919e15e-6cc9-333d-8e0d-a29bca95b9e4 | -0.43614 | -51.76491 | 2025-11-01 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e23c5934-8075-38a9-b043-7dd6d92dcc34 | -3.07785 | -51.24387 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77f4cc05-2c14-3b0e-bace-6b90fd66beda | -0.43126 | -51.75732 | 2025-11-01 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 529ee8e2-2fdc-3a70-8ab0-6c2a77736799 | -1.43155 | -55.44797 | 2025-11-01 05:06:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3688374-0f61-3499-931e-95804cfcabfe | -2.89245 | -48.05886 | 2025-11-01 05:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8361c32f-9ab9-3067-9d01-978f694778b5 | -2.95458 | -51.52409 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5a41d43-a948-344c-a81c-26deadef1126 | -3.4159 | -49.9989 | 2025-11-01 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6297153b-80bc-3ac6-a82a-e1a684885bb5 | -3.15968 | -50.82618 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4474f5eb-315d-3f7c-8b10-d2f232db07c3 | -0.43063 | -51.76128 | 2025-11-01 05:06:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e891774-c983-344d-9849-4bfc73ef633e | -3.23017 | -50.64882 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b60d8b6-f7c6-3365-87e6-246145caed1c | -3.41537 | -50.00249 | 2025-11-01 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2212dd2-5943-39f7-b2ab-a5f8b62881fc | -3.23206 | -50.58363 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 16ea3f12-d4c6-3dfe-a78d-c9d3a3158b80 | 0.50236 | -50.7641 | 2025-11-01 05:06:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ea91189-b0ef-34f0-8ba9-7e6e6bd0afdc | -2.95588 | -51.52546 | 2025-11-01 05:06:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91978f96-04bb-3a4f-89a4-968c9eb1072f | -3.41182 | -49.99828 | 2025-11-01 05:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a61bc578-0a1d-3f6c-81d0-81a8a3ed8651 | 0.50306 | -50.76843 | 2025-11-01 05:06:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72fddeae-1788-312e-94e6-c41df701faa0 | 0.5016 | -50.77122 | 2025-11-01 05:06:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4aaf699-66b8-388f-9504-a94ba0a36de1 | 1.31445 | -51.20674 | 2025-11-01 05:06:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f52e4bb-dce2-3933-86d4-246c947fa634 | -1.93583 | -54.18442 | 2025-11-01 05:06:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec2bb874-f142-3215-8b0c-933bc6ba0ff4 | -1.49505 | -53.12359 | 2025-11-01 05:06:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f41e87bd-4355-3197-9bc1-f04f08d93827 | -2.79425 | -43.34792 | 2025-11-01 05:06:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45d4e889-0309-3a31-b220-64d33d17e003 | -3.22421 | -50.58242 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b6fcdbad-7eef-3d38-a172-a624d0bcaa05 | -2.52478 | -45.84726 | 2025-11-01 05:06:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53cf9754-182b-388d-9ddd-649381329968 | -3.43435 | -42.54103 | 2025-11-01 05:06:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d51e8c0-a64a-3622-82ed-26194b72fba1 | -3.15446 | -50.82828 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef04fde6-ae71-32b8-9fa4-75fcde7a7660 | -3.22814 | -50.58303 | 2025-11-01 05:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e383f1e9-0a07-3509-933f-c7792a34219b | -3.11051 | -45.23082 | 2025-11-01 05:06:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2854674e-80c7-39b1-afaf-23de1ef6cc3c | -2.79502 | -43.34288 | 2025-11-01 05:06:00 | NPP-375D | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12c8ae57-3780-3ee9-9ac9-579914534bac | -2.04973 | -52.0775 | 2025-11-01 05:06:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfe3abdb-f7b8-3bd6-8257-5012e5ac9ebd | -3.88774 | -47.17805 | 2025-11-01 05:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README25.md)
