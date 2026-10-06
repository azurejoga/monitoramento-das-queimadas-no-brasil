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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2da875e2-f1e0-3bbd-81e8-d8b13a3c53cd | -8.86276 | -66.79251 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5b9fd2d-d5f8-33e2-a5da-112cecd38b91 | -11.99813 | -60.47372 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02806a55-9f13-3878-a790-cbdcbcd06674 | -9.34256 | -64.71037 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a1f77290-e56b-318d-bd80-b25eddf6ff6d | -4.28415 | -55.76209 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 674bd0fa-a5dd-3e2e-a8bd-dfebd0e2c721 | -3.67182 | -60.61595 | 2026-10-06 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 835c4ef3-fb81-3734-8145-7de791814675 | -9.49245 | -63.95329 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a1d6a0c-7b75-3959-ae2a-1ccfc68996a1 | -9.6735 | -66.82167 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84da7b9a-2713-3845-a250-0bd3e3fac932 | -9.46216 | -64.33288 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82cb335a-b9f6-3d3c-84f3-3fed73ba9f97 | -8.72475 | -68.90368 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3d1edb2-bcdb-3dbe-90ff-fb47454b4f46 | -3.67998 | -59.62802 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14996154-cf37-31c3-bdfc-6ad229eeb8fe | -3.72096 | -59.69078 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22a3e3a8-b01b-3654-a611-3b406ddd676b | -12.13103 | -61.14862 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecfadb6f-887d-36d7-a24f-a9da3083e002 | -3.98012 | -59.33786 | 2026-10-06 05:25:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee3ed1cf-de58-3543-9e38-79862e460a4b | -9.48724 | -63.95332 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc74dff4-6e7e-33b3-9510-52c3a21f56c3 | -9.09497 | -65.48318 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee519b6f-c409-3b5a-8f4f-02e29a86196e | -12.13239 | -63.16069 | 2026-10-06 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9528d646-4778-3377-9555-b07bf5e334a9 | -3.71568 | -59.33232 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77a32002-c15a-30f1-94de-76ebcdf42c5f | -3.71055 | -58.92631 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec188b0a-13e3-3a48-a340-4e63ea6411c5 | -8.60516 | -72.73178 | 2026-10-06 05:25:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc0994ab-b6ed-3ce0-b23a-52672e4924fb | -12.13296 | -63.1571 | 2026-10-06 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 610604af-d205-3f5f-89d1-8b5eba28c5b7 | -9.73098 | -65.08691 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1a0ec120-b135-3706-a4aa-06f7efe2f14b | -5.81312 | -53.84232 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6f191c4-7e7a-3c61-a2ee-272e0559a288 | -4.5708 | -54.9528 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d326a975-03b8-36fd-9342-cec2b2bf34ba | -6.32833 | -55.32075 | 2026-10-06 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df192477-31f6-35f5-91ee-cb43d1d7762a | -9.48657 | -67.6701 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 722d8987-1c98-3ede-b55e-a45f426aa489 | -9.48767 | -63.96052 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cc95455-1025-3528-8caa-dcc61945d255 | -4.45939 | -54.97463 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aaeec5eb-e67b-3eed-9d4d-65f4b982e76e | -9.15809 | -68.2595 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6893b8a8-f7b4-3344-abb3-aadefd1c242e | -9.11199 | -65.35732 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc693060-7686-3a2a-91c6-e7acb6bada80 | -4.56349 | -54.95287 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5477bea7-a198-3e18-87a4-4bd74a9de2ad | -9.26093 | -65.44499 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 531f6cc8-90e9-3d8a-948a-7e32def7f466 | -9.6011 | -62.38506 | 2026-10-06 05:25:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e847b7fe-8b9b-3c19-a73e-c43fd5f33166 | -5.67813 | -53.5026 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3dea9a0-8e54-3265-9a9e-f7073e3c22c3 | -13.52015 | -61.13455 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b68a324-6594-3d77-85a3-613f8a13a8b6 | -9.5462 | -65.68946 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 994257cc-632d-3402-9a9b-1c82dcc4481d | -3.7866 | -59.37945 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a801501-5080-329a-aabe-36c79762204a | -9.09876 | -65.48383 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af37fa14-b041-3c43-aec3-70e69d4b340d | -8.85863 | -66.79181 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54119f84-97f4-3d6b-b1bb-06954644ec13 | -4.45691 | -54.96275 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e931b181-f310-3771-b35b-f26b408a6410 | -4.4676 | -54.97588 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e5d4c69-455a-34f5-93f2-f8e7aa72c910 | -7.81472 | -72.83383 | 2026-10-06 05:25:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2f5bfed-b143-35a6-a658-d4b481873797 | -9.1396 | -67.81903 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51386f8b-0ce5-347e-8448-1e5dd856be2a | -4.5755 | -54.94936 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db7f4f02-7c1b-32cd-af94-859d29ea7e84 | -11.99421 | -60.47684 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db2db67b-2be0-33f1-af99-e3df48505dbc | -12.13021 | -63.15296 | 2026-10-06 05:25:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56148bcb-188a-30f5-bb48-7f52dbdd4fec | -3.71279 | -58.93389 | 2026-10-06 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed3f961e-ba6a-3d9a-b700-96069512cf6e | -9.1292 | -68.21165 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45537f70-25bb-399e-a847-d9e17574b89e | -4.45794 | -54.96282 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2f9e323-bfc9-318a-b1e3-fd7e5150eee2 | -9.38179 | -68.32898 | 2026-10-06 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af4dc4ac-3b33-301c-8432-1aea7ecad9ae | -9.10571 | -68.31789 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60308e62-835c-334f-9521-19357c59733e | -4.5676 | -54.95351 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8d8718d-8561-3190-98ef-742b7c29d8c3 | -3.54012 | -60.52427 | 2026-10-06 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dbfeaa3-b858-3b97-9929-2547e98e150a | -9.73045 | -65.09311 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 5addeb9b-69b9-37ee-b9a8-ec0c6938145c | -9.09233 | -65.38245 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee9c688c-2b78-3d95-a72b-0293bab9cffb | -8.84974 | -66.7942 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7099a1a0-e48a-30c9-8d64-beccae13a8aa | -9.71502 | -65.09509 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c430205-e96e-38e4-be87-8e9648208399 | -4.45992 | -54.97096 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ce0d278-a78f-321e-8aa1-12b3f2393a98 | -9.10882 | -67.81368 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 227e4306-6a05-3cdd-9a15-a6047ab25545 | -9.40437 | -68.34057 | 2026-10-06 05:25:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6f071fa-8a1d-3f1e-a726-806ac17522e7 | -4.46813 | -54.97227 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37ed8944-91e0-354f-ac3f-6909dda607af | -10.24583 | -68.30385 | 2026-10-06 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e7fe996-8f1f-3de5-a59a-9b785c1fd1c3 | -9.15891 | -68.25484 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a3e17af-c0b9-3d64-b698-25bed396f119 | -4.91909 | -55.8661 | 2026-10-06 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 034ff179-3792-37c7-9aa1-b4f544d33ea8 | -9.13372 | -68.21244 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b19d6ee2-243b-30a9-983a-cfb5a0d77134 | -8.93683 | -67.34834 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51546497-d558-3684-8dfd-b53d0b8bd16a | -3.79046 | -59.37649 | 2026-10-06 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 687f8c11-8e6b-372e-9aa6-7419956cd304 | -11.99243 | -60.47712 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5912170e-88ef-3407-9f52-e3d364e180db | -9.29312 | -65.64806 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7541ddf8-befe-334e-b529-28c90929f966 | -9.59971 | -61.83171 | 2026-10-06 05:25:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74819156-f353-3390-a214-6f320af2d65e | -9.11371 | -67.70806 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 888a4d0f-18a1-332b-b4b3-ec2feb49099a | -10.27887 | -60.54524 | 2026-10-06 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05d12b1f-c9f2-35f5-b2ed-cc9a800073a0 | -9.44464 | -67.42927 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1662dd3e-6b93-3e40-b42d-144ac79374ed | -10.27942 | -60.54167 | 2026-10-06 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f4d1c73-086d-3ef2-9827-c4c32429b8eb | -9.02469 | -65.71566 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 12904ed6-1035-3c1b-93da-40d5a242a875 | -13.52347 | -61.11275 | 2026-10-06 05:25:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24d0b027-dc2a-3dcb-9135-0d55f6d82ef0 | -4.56256 | -54.95157 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee512afa-1358-36ff-b935-18caa9c34aab | -10.44306 | -67.89955 | 2026-10-06 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e960b520-478d-3455-9c3f-b6f596819fa8 | -9.11028 | -68.31862 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 83da82c4-727e-376d-97f0-0d27a2d010e7 | -9.97203 | -65.01762 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 960b41bc-14e0-31d4-9530-bfee0b478e7e | -9.13253 | -68.24558 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c56a825-75c7-3179-bf1e-0a3b38430ddf | -4.46156 | -54.95962 | 2026-10-06 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb982a9b-b585-3490-843e-cca0765064c0 | -9.67694 | -66.82607 | 2026-10-06 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 710759e5-14a9-3f8a-83f6-c4779ccbe438 | -5.82477 | -53.85806 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73339302-1bff-3e35-8c4e-587a7438c4be | -9.50388 | -68.49652 | 2026-10-06 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0ae3c41-acc8-3747-af97-c671075851d3 | -9.82773 | -65.04933 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4cd6bb4d-cdf6-315b-9165-14e1352ab1d6 | -9.10211 | -67.69727 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cf60df2-bcf2-3d74-9bc4-a8d5340100c5 | -10.47688 | -67.86987 | 2026-10-06 05:25:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af70b590-665b-3b0a-b6db-c5a6233aa415 | -9.1255 | -68.2063 | 2026-10-06 05:25:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 138139e5-9dd7-30d3-a48f-4c573e5d0337 | -9.73117 | -65.08868 | 2026-10-06 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 10caafb8-09c2-30b5-b954-11875d2179f0 | -5.82215 | -53.81085 | 2026-10-06 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2187f29b-3e33-3c9f-81c6-126669e15288 | 2.73877 | -60.25411 | 2026-10-06 05:57:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65a2fcda-8227-3521-ab0b-dee1750e3642 | 0.31433 | -60.44178 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd993c5-2a45-33b8-bc7f-42c5a0eacc55 | 3.55888 | -61.3373 | 2026-10-06 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f04b69a-cf27-3f8b-aebe-1f4daa638a81 | 0.86298 | -59.70197 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37cde469-90f0-33d7-bd03-e2bd24e0e7d8 | 0.91517 | -59.54564 | 2026-10-06 05:57:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ae0b4ad-71fe-3a97-93b1-7367f484f091 | 0.44529 | -60.53944 | 2026-10-06 05:57:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f3faa3a9-fb6f-3a6d-a640-47767d1707e8 | 1.9859 | -60.61881 | 2026-10-06 05:57:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 491f57aa-2a05-3f0b-bc8e-dcfa35a75e7d | 1.72652 | -55.62848 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b54709a-41f4-3ab2-a5ad-53d247aace77 | 2.46163 | -50.83888 | 2026-10-06 05:57:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 94807af4-d4c4-34f8-98df-d12d551af22f | 1.71767 | -55.64718 | 2026-10-06 05:57:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README67.md)
