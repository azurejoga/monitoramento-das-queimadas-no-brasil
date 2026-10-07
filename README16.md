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
| 07a0a57f-e2d0-3f5e-b34c-668de4468f4f | -4.1477 | -54.0355 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d27a36ce-1add-39be-9411-0ad81015fbdb | 0.4495 | -60.5303 | 2026-10-07 01:09:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d0a14453-6e2f-3683-9c5d-4ef57448b86b | -14.2563 | -41.637299 | 2026-10-07 01:09:00 | METOP-C | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 12724fcf-5c44-3508-b313-430ff01d02a6 | -3.2424 | -53.868698 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0711800-d0da-3f91-9fa4-16f6b9312d9d | -2.7756 | -54.0783 | 2026-10-07 01:09:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e80b1cdc-ab36-3e95-a21e-c4efdeefe75f | -11.7914 | -46.597401 | 2026-10-07 01:09:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e83260bd-7a42-3664-ab51-eb243ce609a6 | -11.7351 | -43.641602 | 2026-10-07 01:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ccd37936-c2e1-322f-b1b4-4a87fb3fb745 | 2.4396 | -50.847198 | 2026-10-07 01:09:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb02959-1246-3e12-aa65-5e5447c47c7a | -1.1262 | -54.121399 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c516ff4-a9cd-3eb2-bdc0-2317ee34a16a | -2.5985 | -57.551998 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af6c14a1-9826-3ef4-8616-79f2fb0aabfd | -3.6733 | -57.067699 | 2026-10-07 01:09:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c062749-a24f-3bb7-8014-b9f99fafc274 | -2.9728 | -56.622501 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4d83c22-171f-3917-8ec4-f7b0fa244331 | -3.7315 | -59.445999 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b27496b8-6c7d-388f-b6d5-0bfe7b3a508a | -5.9635 | -55.366199 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 111b8d54-d048-387b-b705-c3be98955289 | -12.1759 | -44.695499 | 2026-10-07 01:09:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9b023c7-5219-3349-81c6-1617c8809111 | -3.6748 | -57.0746 | 2026-10-07 01:09:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c52965d5-7724-3ae5-9a11-0109bc392f28 | -3.1966 | -50.571201 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b064f60-5923-32c4-bf0b-57f4640f64a8 | -3.374 | -58.192299 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edeef65a-9651-3d55-b662-129d162f39ee | -3.5469 | -59.494801 | 2026-10-07 01:09:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72065af1-8e02-3a90-8f6d-23d9dc4bf7fb | -11.0612 | -45.819302 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 39fe3f8a-e656-39d7-8253-d70502e0cd66 | -2.7011 | -59.804699 | 2026-10-07 01:09:00 | METOP-C | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8cbaab5-979e-34d8-b66f-135e82c454e9 | -2.828 | -54.126099 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a07c131f-f3c2-3828-8919-536a8e575dc2 | -2.8299 | -54.134201 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb3c251-1c25-38ff-8935-fcfc069cee75 | -4.2703 | -54.871899 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc92cb62-310b-39b0-81e3-097d566a451f | -2.7833 | -51.692402 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67224aef-cad8-3428-be07-3b5b0cf35ae9 | -2.6048 | -57.5793 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a04dc0f4-80ca-3eb0-b39e-f016ed207d30 | -4.7642 | -55.667702 | 2026-10-07 01:09:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e33d7dc-cc0a-3a89-a112-75112bc8da00 | -6.2206 | -52.845402 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71253dd2-ed23-3f48-84d6-9fc75aeb493e | -3.593 | -54.310902 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86bb3697-8661-3601-99cd-4b5e97219677 | -3.2683 | -54.068298 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12e41465-767c-3ef2-ada0-27f9e28d39a2 | -2.9851 | -54.047798 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbe7d7b8-af3d-37d8-b724-4d3f489c30e9 | -3.5703 | -54.478901 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98fc512e-a8b0-3231-be5e-c8f5b0a5d87b | -3.1331 | -53.709999 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e49e7cf5-9942-3706-a66d-d3b85c1e1c1b | 0.7195 | -51.385201 | 2026-10-07 01:09:00 | METOP-C | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3fbce1-6540-3a67-b51d-0e408939ac2a | 2.0092 | -61.097198 | 2026-10-07 01:09:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6e44a32d-9287-33a4-b459-67e365d023ca | -13.5035 | -44.3717 | 2026-10-07 01:09:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 51a6655d-54a1-39cd-87c6-5297309920f6 | -3.2757 | -50.428101 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff14f6de-14ea-342f-b59d-20f635ba784f | -1.1124 | -54.151001 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f29c95c9-738e-3c9e-9167-237d75630191 | -3.4933 | -50.091 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8916dfd-c7a5-3f99-a283-16b57f4b6da6 | -3.0137 | -54.126301 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53521336-9400-35cd-9e16-85f168098ced | -4.4576 | -54.967602 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd24a6c0-8221-3efa-ba46-fa3187cb820a | -3.0477 | -54.228001 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d02ef10-75fb-36a6-ade8-8c128ba7ca1d | -3.0118 | -54.118301 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3be517c9-f5e9-3b04-ae2b-9c80fbae72fd | 2.0208 | -61.0914 | 2026-10-07 01:09:00 | METOP-C | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ca865bc4-4554-3d34-ac5e-ad904eb677c4 | -1.301 | -54.564999 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9884d26d-d27d-307b-b84d-5dd967c52147 | -3.9674 | -56.059299 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49526304-cce5-3440-a002-f0c5205d9b4e | -3.0556 | -57.521702 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8140619-0972-3907-883e-1778b9b424ba | -3.7445 | -51.230701 | 2026-10-07 01:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d016dd4-68ca-3a39-8fe9-db1490f16fb3 | -3.1089 | -54.1805 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1aa4e90-43e2-3825-912f-63c8a3442f23 | -11.235 | -44.880001 | 2026-10-07 01:09:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 097859e2-1d62-3ce4-afb9-e01720f4bb59 | -2.3768 | -56.140301 | 2026-10-07 01:09:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4df5946-f839-31b1-80be-2e0d2861c3b6 | -3.4739 | -50.0956 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be7e6cd-3c40-3bde-b63e-ddc122a2931e | -3.1053 | -54.298199 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c0fa02-7194-368d-aa1a-a6a91dc30eb1 | -3.514 | -54.636101 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd54e1f1-90b3-3381-9015-3e58368ba7ac | -3.0331 | -54.52 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7df180d7-8895-3f6f-9baa-c7c74cb1fec4 | -10.8511 | -50.663601 | 2026-10-07 01:09:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46bb1e85-8029-3ed9-a098-31a38c3c6e91 | -2.8864 | -54.1553 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e95da0c3-4c74-3ba7-be12-516d5e01053d | -6.7833 | -56.239399 | 2026-10-07 01:09:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 132b4484-a2c4-394a-8fc8-1211eb424ca6 | -3.0818 | -54.153 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9315517-4355-35db-9547-ac860239b1c4 | -2.8533 | -59.116402 | 2026-10-07 01:09:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c726b59a-8ffb-3b4b-8e58-bbdb9ab46a31 | -3.4776 | -59.461498 | 2026-10-07 01:09:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c97440be-b4e3-3e43-84d7-d20391777637 | -3.0272 | -53.8745 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d40fba84-2281-315a-b6a1-cb7fa0d11485 | -2.9052 | -54.014599 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4523a830-2e80-3951-894b-aabf4b79cd7f | -7.8522 | -44.176102 | 2026-10-07 01:09:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3752da45-6c9d-3aed-b11f-687dc8c59798 | -3.6871 | -55.962299 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37b97b17-0539-3e95-ba10-17d19021088b | -2.9587 | -54.155701 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 022c5c0f-790c-3b2c-b1bc-42ad812d9b8b | -4.3742 | -55.453602 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71f9eb38-c17d-34ab-984a-7be7e57601bf | -3.0839 | -54.2948 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87cd9c37-ceab-39dd-ba64-2ef28f862e38 | -3.0593 | -54.2337 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10506850-b1c5-3ad1-a405-946671a95bcd | -3.19 | -50.586498 | 2026-10-07 01:09:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19f21e95-bbf5-3d6a-a1aa-110af6a356cd | 3.1477 | -60.5909 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bc143d9a-e607-32d5-adbf-63238dde24ea | -3.305 | -53.871799 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2259084-24f2-3d43-8ffa-c5fc6d797f17 | -3.1421 | -51.034199 | 2026-10-07 01:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b146351b-bc97-3bc5-84d4-25eabef95a55 | -6.0032 | -53.499298 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da15a94a-748e-3e5d-aec5-cd643053a2ee | -2.4268 | -56.536201 | 2026-10-07 01:09:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f89bb36-aff6-3540-8358-2b4c5928bbce | -3.5622 | -54.4888 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541242a4-575d-339a-a661-2036a688e562 | -4.3506 | -55.128899 | 2026-10-07 01:09:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2128cd57-10f9-3516-9805-6240218ab0ba | -6.5857 | -53.0364 | 2026-10-07 01:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a3a593-1e92-300f-8623-a6c686829033 | -3.5388 | -54.6544 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 051d8de8-cc43-38d6-82a0-570c647a7c16 | -3.3293 | -54.1973 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4147f47d-368f-3eeb-886b-1663231fd3c1 | -3.0572 | -57.528599 | 2026-10-07 01:09:00 | METOP-C | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc2a634a-d347-3675-b4c7-fb3e9d5aaead | -3.2981 | -54.0191 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c4de401-731e-36cc-be0c-a9138038b8d8 | -3.1174 | -53.7752 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec3dfa7-e227-305d-8e66-3801cfc92133 | -3.0955 | -54.300499 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce334d5-03f8-3d40-b5e8-106ca78da921 | -2.9297 | -54.119999 | 2026-10-07 01:09:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca31abe5-d291-3654-a289-b691b7a5e9f0 | -3.8583 | -55.9893 | 2026-10-07 01:09:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7eda793-957b-3668-a2d4-10bcd5fd3c2f | -11.1014 | -45.698101 | 2026-10-07 01:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5c3bcbd0-32f0-3287-8151-863b0f863d43 | -3.4891 | -57.793499 | 2026-10-07 01:09:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac9c67d8-f939-356a-b59c-b792328a5e62 | -2.7476 | -57.662498 | 2026-10-07 01:09:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13960c9c-03a3-3797-bf3e-2b6fd898f8ea | -2.3271 | -57.9874 | 2026-10-07 01:09:00 | METOP-C | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe36caf-3db9-3c0b-87c2-b03b0404d679 | -3.0523 | -53.938 | 2026-10-07 01:09:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 218124c2-3c1e-3c19-8e2e-c7d3705dc118 | -10.8899 | -46.665699 | 2026-10-07 01:09:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd610104-d44c-390e-a8dc-0ddacb4c62ad | -6.0069 | -53.515301 | 2026-10-07 01:09:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c91f6f4-f3b1-3e77-9c3f-8e87cc00e855 | -3.082 | -54.2869 | 2026-10-07 01:09:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0182848c-be18-34a9-9872-cb98eaf281bd | -1.5074 | -54.832699 | 2026-10-07 01:09:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcf3ca48-59be-310b-9fd0-4dcba36e85e5 | -1.0968 | -54.127998 | 2026-10-07 01:09:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddaa120-75db-3bb4-b14e-5d3b0e5ce925 | -6.763 | -55.4772 | 2026-10-07 01:09:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5a87e6-40f3-3cf6-98aa-a5c27fea06ff | -9.8031 | -48.9291 | 2026-10-07 01:09:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb886c49-d44b-3af9-a03e-485fd917be59 | -3.4828 | -54.635201 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bef9f02-3099-3ee2-92fc-5dd6f9b3bd98 | -4.3656 | -54.749401 | 2026-10-07 01:09:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
