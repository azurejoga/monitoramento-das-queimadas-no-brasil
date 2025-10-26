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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 194f960a-077b-3ac6-9307-03f578bd5496 | -8.7229 | -48.01041 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3681a748-b63d-31f1-83d7-02bfbf39132a | -10.80536 | -47.873 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8063c23-5f93-3797-a1d8-d62fd0326f44 | -13.40625 | -43.02303 | 2025-10-26 04:51:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d75a58e5-9e7f-3bed-9194-cca2e5eb99dd | -8.3147 | -46.81604 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed004d48-0d33-300f-89ac-3cc63de7dda3 | -14.77423 | -44.97537 | 2025-10-26 04:51:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6740b7c2-fa22-3111-bd36-ef1407812355 | -13.88339 | -48.47786 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6142088-46e1-33bc-8d13-cfe1e65fba8d | -12.02222 | -43.30624 | 2025-10-26 04:51:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 548bca1e-71c3-3772-9023-4195b09f5b63 | -7.69054 | -42.18857 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1cf344cd-bf33-3432-8026-99883c0052f5 | -11.51004 | -48.23946 | 2025-10-26 04:51:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c1d92bc-e9ff-35c4-85ab-347b1358add3 | -13.91814 | -48.37555 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c61e462-4764-3c40-a406-45dbf1aa1a50 | -8.9275 | -47.68409 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b86fd6fa-57f3-38b6-b4fa-dafe38b6889b | -7.96562 | -45.16358 | 2025-10-26 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce36e6a8-45c7-3c12-90f8-cb2668555834 | -11.69819 | -55.46246 | 2025-10-26 04:51:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3543796-90a2-33a7-be30-e3fb4c2f778a | -13.28628 | -47.50684 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d748bc29-7aaf-3e6f-a3a3-0c494646e57a | -6.80914 | -49.3507 | 2025-10-26 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9adc7d1e-8747-3047-a0c7-eb2fc9a04738 | -8.63109 | -54.89123 | 2025-10-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41927b44-777f-3353-b631-32d3df2ec1f6 | -8.11966 | -44.80439 | 2025-10-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e408fe2e-5f2c-37f6-a442-58cd7a7b51e6 | -7.73844 | -47.01146 | 2025-10-26 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a40d19f-8b57-3a86-b486-f8ffe69302af | -9.18199 | -57.69128 | 2025-10-26 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e812672-74e3-3f87-8136-361358ede6e6 | -8.15351 | -47.03937 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e070784d-67ab-3fe0-b613-df43f9669a26 | -8.31959 | -46.81269 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c7baa40-2e3d-345f-9768-9fb72bc99fb0 | -11.39995 | -54.69372 | 2025-10-26 04:51:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0123312a-7afd-3088-9b67-d4f2e81df056 | -13.53349 | -49.54744 | 2025-10-26 04:51:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5b29f3d-9baa-3085-b610-9ff3fe811963 | -10.42674 | -44.49576 | 2025-10-26 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 418340db-4924-35fd-b713-fd1e85630b81 | -10.60685 | -57.76567 | 2025-10-26 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 337b9891-0def-3074-aee7-a68902b9fd1a | -9.09267 | -49.64224 | 2025-10-26 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b12fbf08-3da7-3bbd-9fe4-e827fa1e062b | -11.02559 | -47.81218 | 2025-10-26 04:51:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f99a810-7f1b-31f6-a2f4-76dcd81078a2 | -8.14927 | -47.03872 | 2025-10-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d5897cd-30bf-302c-901e-50a21aeb8fd4 | -11.04987 | -48.31963 | 2025-10-26 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db7a092a-2915-3ced-9bb5-fd82636c9534 | -10.87495 | -50.14017 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed64fb56-d102-33bd-8553-bebd30fe7b27 | -8.71888 | -48.00984 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64b3e5b5-199f-3048-9872-c43f1dd89d72 | -13.85467 | -48.50211 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06df9f84-39b6-30d3-af85-a257d15ffdd8 | -12.83946 | -48.65836 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baced7d6-5870-3a4e-83d4-9426daf1ca6b | -12.06231 | -43.98886 | 2025-10-26 04:51:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd03bd7b-d521-31f2-8e21-ecbbde1ed55a | -13.26851 | -54.39502 | 2025-10-26 04:51:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 895309bd-a861-3e10-8375-19d76bcd3cf2 | -13.92515 | -48.42016 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a620c410-1daa-36e5-af75-5357368ee66d | -7.64842 | -46.27806 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60c4a928-b67b-3c1e-a01a-db9561fb3ce6 | -14.19272 | -48.19022 | 2025-10-26 04:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbc85558-c947-3e73-a3ba-a78242adafde | -10.82314 | -47.06797 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37f97877-6123-3a46-bc28-623f38864b5f | -8.30248 | -42.30779 | 2025-10-26 04:51:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3638342-15b8-3669-97e0-9573b0573573 | -10.27682 | -53.98787 | 2025-10-26 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 507be2d2-0930-3f29-9d0e-0776e9ae6a8c | -10.94678 | -48.07381 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eb838b68-867e-3486-8af8-28507948a6af | -10.22161 | -49.84911 | 2025-10-26 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1b6fffa-835a-3d82-8a61-415e68ff0662 | -13.29614 | -47.50056 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 31b0edfd-fd8e-3eb7-9d24-867a3451e0f4 | -7.88673 | -45.71279 | 2025-10-26 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0ce06c1-076f-3bb4-b900-90d73074be62 | -10.83018 | -47.63435 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bb9cafa-262f-3197-8784-148ed7a9c18f | -7.88295 | -45.71445 | 2025-10-26 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e5f565de-fd63-3f26-bf4f-e6a4dffc52c6 | -11.53219 | -47.10347 | 2025-10-26 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 303079fc-befd-3d1c-b2a6-dab00c0d18ee | -10.95091 | -48.07442 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7e2c9877-b44f-3448-a126-972b98046441 | -7.00142 | -50.83508 | 2025-10-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 43a8fa18-124a-3830-bb90-fa6810c39f4c | -12.3708 | -48.10762 | 2025-10-26 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42146db7-9773-33b0-b935-f83c8c8c83d2 | -10.87834 | -48.03108 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e4d32d5-667f-30ee-ab2c-ef97154228fb | -11.88188 | -56.40232 | 2025-10-26 04:51:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5538892-2c57-3c8e-b858-3b29417ce91d | -8.34143 | -48.17852 | 2025-10-26 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2110b6d6-fa11-39aa-89d3-ab3852ac62e8 | -14.76925 | -44.97118 | 2025-10-26 04:51:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee2348c4-7af1-3d49-b91f-1ab684703d83 | -12.04486 | -54.23336 | 2025-10-26 04:51:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e20184e-305b-358a-ba2c-332c3651f5f3 | -13.23306 | -47.745 | 2025-10-26 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a170db6-f486-3ddc-b4b8-616642291697 | -9.45233 | -56.64679 | 2025-10-26 04:51:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 535a3f31-f158-329b-a3fd-e63b499ca1f9 | -11.39703 | -46.06419 | 2025-10-26 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b97de8d-1925-38e6-8608-8f81221c1082 | -14.77383 | -44.9789 | 2025-10-26 04:51:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9b907da-446c-3fa0-9f13-6e59ee8848e5 | -9.11819 | -45.85215 | 2025-10-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49391264-0e03-3d90-a252-95da5440f98b | -9.22188 | -50.75694 | 2025-10-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1539f63-7aa5-3ce0-9aae-9b5c22c0e550 | -8.04892 | -46.74805 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6ce75b45-4213-3401-b816-cefa414d1f87 | -9.72598 | -54.62178 | 2025-10-26 04:51:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 299e8049-c09d-375b-8cf0-b46b2ca540e3 | -10.88656 | -48.03271 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35e9c53d-c3a1-3da2-a6c3-f6996f7b42d6 | -10.89793 | -48.0301 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a04e2a8c-3489-3c0b-88f9-e699bfc59044 | -12.09483 | -47.25435 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15e1bd3a-85bb-32a2-bbcd-d0780b502da6 | -12.85404 | -48.64326 | 2025-10-26 04:51:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cb36509-437e-3c6c-bb9d-6bad6589b851 | -10.41012 | -45.31138 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dd2a7beb-0bef-380c-9393-6c26932787e5 | -9.92605 | -47.64679 | 2025-10-26 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37702741-10df-3b24-8194-f9e023c3b7de | -8.72732 | -49.61006 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7b80890-4d20-3c89-a54c-7b349c21fa4e | -10.83126 | -47.62658 | 2025-10-26 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84fa4033-a361-3cb6-98bb-891be18d569d | -13.9272 | -48.40471 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db894e37-9bbd-3c09-bd79-cf853c119e44 | -10.99067 | -44.86751 | 2025-10-26 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5338d0f-63a9-3ac2-9a80-a07f6823c96c | -13.32186 | -47.92544 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2962cb83-2294-3387-8965-e2a56dc65147 | -11.06399 | -48.33719 | 2025-10-26 04:51:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8da436cd-907f-3179-9702-e56fbcd36bdf | -7.8462 | -46.43739 | 2025-10-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8db8195d-d8ad-395a-9d01-919565535c3f | -7.78766 | -45.38964 | 2025-10-26 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ddc138f-7157-3574-a4fa-9b8b4e7669aa | -13.87567 | -48.47141 | 2025-10-26 04:51:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cf90143-9d96-38e9-ac50-3043c04503d8 | -12.10721 | -52.48933 | 2025-10-26 04:51:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73f013f6-827d-37b7-a8b0-0edf63f47bbc | -12.88888 | -54.72799 | 2025-10-26 04:51:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00c5440b-87fb-364b-a084-4c3f6c843f06 | -10.40855 | -45.31109 | 2025-10-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c493550-f08d-3e68-8628-24d2b979467e | -11.56397 | -54.51956 | 2025-10-26 04:51:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f729fcea-f526-3f59-a530-7b0adb4b3dd1 | -7.84562 | -46.44151 | 2025-10-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dccace84-3b7c-3635-9c83-88d11065caca | -14.50512 | -43.00312 | 2025-10-26 04:51:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 28.8 |
| d5b8c649-d8d0-3c98-8036-e6e0e6c01952 | -10.4067 | -44.73734 | 2025-10-26 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f57d289-0e87-3296-b6e5-b4d26d76e4ed | -10.94266 | -48.07317 | 2025-10-26 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a554d8f6-67cf-3d5a-a518-9b74a9ca2af8 | -11.69879 | -55.45876 | 2025-10-26 04:51:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c83dec2-5d32-301e-9666-e081ae953f73 | -13.32612 | -47.92649 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 157bea82-29d2-3735-8f0b-644ae6ce2624 | -10.89729 | -50.1655 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e109c88-4fc8-32a9-b5fb-1e91f747d1fc | -13.3272 | -47.91822 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad7a5795-d862-3b9b-bd02-06f98828566b | -6.81119 | -49.35282 | 2025-10-26 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15a8b7ea-e233-37f3-b9e8-28ec5746a71f | -13.19636 | -48.44701 | 2025-10-26 04:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3957d8ba-3f7f-3c72-b405-eec94ded313c | -11.09562 | -55.55925 | 2025-10-26 04:51:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8013399-d7b6-3476-bf97-b375e647ea42 | -13.33306 | -47.90705 | 2025-10-26 04:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71949f7d-49f8-39f5-874f-a9c3c0b5508a | -12.32101 | -47.48066 | 2025-10-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ee8a17a-fc0f-3fea-90f3-d7b356a0d1bc | -10.94392 | -50.28414 | 2025-10-26 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feb5a0a6-cdc4-30d6-ae42-70ad41645bdb | -7.99626 | -46.71421 | 2025-10-26 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07bb737d-549d-36ce-9a1a-b8dfa4b9084d | -8.69386 | -50.82177 | 2025-10-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c815f9cd-e840-35af-9e69-edfca457ddda | -7.69753 | -42.18108 | 2025-10-26 04:51:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
