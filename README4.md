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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 329893c8-3df8-30a3-97c2-8dfe6a50cbce | -3.2634 | -54.0499 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 403a1f18-cb7b-35f4-b295-31fe55bfcb3f | -3.0054 | -54.136398 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023281de-8bef-3707-8d67-7eed20537ffc | -3.1065 | -54.175301 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1b118a3-ee36-355b-8bf1-c7f9b01bce04 | -7.4542 | -42.839699 | 2026-10-09 00:06:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ceede919-266c-3195-831f-0fa233a9c98c | -14.9627 | -47.544998 | 2026-10-09 00:06:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 71c159e0-3620-3281-93aa-827dd2f8a90e | -4.9442 | -45.6642 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd42acf7-cb18-3e63-b276-13d3a54e0ae1 | -11.7637 | -46.784302 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c5535151-5dc4-3f78-99a1-e34d550e1329 | -13.1903 | -54.349701 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 050a4c09-f57d-3147-a945-6b92d7370734 | -2.7434 | -54.112999 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 139c7eb5-343a-3167-bdee-5209d7881322 | -9.9084 | -44.872799 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80fbc46d-d78d-30ea-95f3-4fc65056302d | -11.9987 | -43.491001 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e09f317-ca3e-3fec-b42b-da545a914bee | 3.7431 | -51.6152 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bd34a7fd-658e-33cf-aa91-948d6d909164 | -18.479099 | -42.251598 | 2026-10-09 00:06:00 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ca1aec6-5c4d-341d-8603-0a7154ee41e1 | -5.2335 | -43.989899 | 2026-10-09 00:06:00 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cc4890a-c4c3-399f-8131-49eaa3fcb22c | -13.0275 | -46.8097 | 2026-10-09 00:06:00 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 34d0c823-a7ff-335e-88bc-7bb64bb916dd | -6.4102 | -55.1884 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70387f8b-e2da-3d9d-8cca-39d2b79c7ebe | -4.0604 | -49.102299 | 2026-10-09 00:06:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 899ca7d1-fb97-3454-89c0-1bd982c8d3b3 | -8.9146 | -45.170399 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 10ad0b2e-cf12-3b2f-8d4f-ac9241b3fc54 | -11.4581 | -43.391499 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5256b82d-22bd-37dc-8d7b-f2f89d59b854 | -6.1217 | -55.700699 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e081bd05-910c-3e28-8f80-7fb755bc8b38 | -2.7847 | -57.623501 | 2026-10-09 00:06:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3bf7741-7f67-3eb9-a763-f68934ffdef3 | -11.9111 | -46.570499 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67abf44c-db34-34a8-b51b-fd026b28ad73 | -5.7441 | -43.2733 | 2026-10-09 00:06:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e090e31e-5c1e-396a-adec-123c39755703 | -13.1778 | -54.337601 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64d1a74d-94f9-3d60-84af-b5ac6545526d | -10.8728 | -44.801498 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b7b4921-039b-3716-9624-3b07972ca6ba | -9.119 | -45.8269 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1499b00b-5605-3eda-9887-b200fffd092a | -2.4979 | -56.052101 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aac22b63-ac99-3d08-9bc5-5a76e8c4bafb | -1.3261 | -56.4011 | 2026-10-09 00:06:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 507c1e2d-9db2-39ab-9d90-20be1cadc10c | -17.873699 | -45.9856 | 2026-10-09 00:06:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| de891e6a-7873-3f8e-a2e5-91c4f8b2b2fc | -10.462 | -47.870098 | 2026-10-09 00:06:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fec5df74-bd42-3207-a5a5-38b21b876fa4 | -4.5383 | -47.035198 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d518a9e1-b6a6-3ec9-bf01-96f7e625ef53 | -12.0189 | -43.445999 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74bbadb5-5348-3e4d-8937-4a36621645bc | -4.9922 | -44.984001 | 2026-10-09 00:06:00 | METOP-B | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af74617d-1189-38db-a609-5a8acb2a7f3b | -3.0088 | -54.1054 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99c8fd76-51ad-3479-8ea2-1aa5f32100c3 | -3.3047 | -54.050999 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c639a651-aa17-32ff-99a6-526adb443361 | -4.6419 | -50.9552 | 2026-10-09 00:06:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81ceb438-cfdd-39ec-93c5-ff0e502f770e | -6.152 | -47.914101 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49f8ac58-110e-3b12-95b7-f91542264b6c | -11.0621 | -44.071098 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24499477-d74a-35b1-9c74-93e12419748a | -14.0031 | -48.760201 | 2026-10-09 00:06:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9413130d-d30f-3c8c-be49-7b93817784e5 | -4.2606 | -46.275398 | 2026-10-09 00:06:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a3e51a6-0785-3413-b85f-f27c47dd72f6 | -13.4377 | -50.9333 | 2026-10-09 00:06:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4941e6c5-c39a-30eb-a3c8-86a233fcef2b | -5.9837 | -40.929001 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 236205e1-5161-3572-9034-8cc1908a9603 | -4.667 | -49.2323 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f75fa19-b2e9-30e6-badd-49fffe7de00f | -9.9198 | -44.7896 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c1e973b3-0fe3-3dad-aa4d-a61427b6c5b0 | -2.7532 | -54.110802 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 640fe79d-4d5e-3906-8866-471f484ed562 | -3.0391 | -54.1493 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d103993-3f8e-3d01-9f89-c260475a3913 | -6.4962 | -55.303799 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51433e5b-059a-32b9-a3ce-57a8a139e644 | -11.8635 | -43.5742 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5fd6219e-92c7-3964-b9eb-5ca611142aa4 | -13.5001 | -44.374599 | 2026-10-09 00:06:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99300e9b-880d-3a9e-8ee0-a2e5a0ce49e3 | -6.34 | -43.353199 | 2026-10-09 00:06:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 79567d95-c719-3399-a549-b519dac2f966 | -11.6177 | -43.713402 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9be3367-2c35-324a-adac-e327d24447a5 | -11.6426 | -43.687698 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3151b57-bba1-37e4-bc9c-8c078495edd8 | -5.9896 | -55.370399 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a40bef34-cf14-3b41-9368-04656c635c0b | -6.9795 | -47.652901 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d783a1d-5543-3000-83a8-f7092c17eab4 | -2.8671 | -54.2071 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d428b331-3aa6-3802-bb3f-145cd03ea521 | -8.146 | -49.4459 | 2026-10-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32163b6-8f8e-3a9e-8c4a-0081386fbec5 | -2.8785 | -47.848301 | 2026-10-09 00:06:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037db8cc-8f35-309e-ae97-8de5499eb0b5 | -7.4032 | -44.754501 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49f6875b-8b59-3071-92d0-9c180acad1aa | -3.2962 | -54.0126 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52290483-2857-3dff-b059-a94d0ab0a935 | -7.4765 | -42.846802 | 2026-10-09 00:06:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cbe21137-770e-394c-b8ac-87597e124cd1 | -12.2987 | -47.052898 | 2026-10-09 00:06:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ec1181f-0341-3694-9fba-362ea2e62191 | -17.8267 | -52.349098 | 2026-10-09 00:06:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b756e411-65a2-35fe-bd59-30aa49afa810 | -9.8643 | -47.459 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 235c8bf6-0372-33f4-a67d-8b6a862019ed | -9.2969 | -47.412498 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 731b6cd9-75dd-3097-ad04-98664f9c89b3 | -4.0871 | -44.107101 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f310b4fa-8d57-3ef3-9734-f87476a06d06 | -10.4234 | -47.286701 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3619e477-fcd4-36fe-8369-8012c14d6a47 | -6.1188 | -55.687199 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a2f5458-d69b-3388-a098-31b11b4a137b | -1.6005 | -55.155899 | 2026-10-09 00:06:00 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5bc20c8-091d-3347-b5b3-3efcdc90c4e2 | -2.5022 | -56.117599 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a602e900-5245-37c2-8291-7bcf613c7fb4 | 1.7019 | -55.5928 | 2026-10-09 00:06:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 217468be-bbda-3b04-8348-b666c97197a2 | -8.5954 | -49.5224 | 2026-10-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fcbfef8-de31-3fcb-83d4-1d3f18248e7e | -13.1653 | -54.325401 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5028b76-70a7-3328-8bcc-409ad7adf628 | -8.2163 | -46.431198 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2b0caec-9ec4-3091-87a7-6fd7788c78be | -10.9062 | -45.520599 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 77859633-2b3e-3807-9634-dd1b76fd0cd2 | -5.9919 | -40.9627 | 2026-10-09 00:06:00 | METOP-B | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d7a0db72-3e70-37b1-8804-0699b7dd8457 | -10.0456 | -48.219002 | 2026-10-09 00:06:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5d5d970-b912-397e-b0d0-402e201d5a73 | 0.2986 | -51.389801 | 2026-10-09 00:06:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b75fe0f7-e520-396b-8c1f-1ea1b11cc7e8 | -9.0907 | -45.128899 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 42e1f01a-73f9-36e3-a570-6d7c1c43644d | -13.1805 | -54.3517 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf7574d-d046-3afc-a614-b1e8a72a61b6 | -5.6625 | -46.2286 | 2026-10-09 00:06:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f96396e9-180d-3548-bb96-8ef399556dfe | -3.4573 | -50.587399 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfd1523a-eb06-3622-bd6f-4fe8e5990d81 | -3.0143 | -54.084 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 666f6962-c4fb-395f-b54d-1cdd52cfb136 | -5.0849 | -46.138901 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd15b725-3d8b-313e-aa0e-460bafbc18fc | -7.4053 | -44.763599 | 2026-10-09 00:06:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 411df316-88ef-31ed-ac19-8044587d6ced | -3.9714 | -59.327599 | 2026-10-09 00:06:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3241d5-9d1f-3144-b010-d443a33b5556 | -4.669 | -46.302898 | 2026-10-09 00:06:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2938a226-02e6-3083-baf1-fc74827ab418 | -3.526 | -59.564499 | 2026-10-09 00:06:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3487d7-c404-36d2-8eda-afc6553fc276 | -4.9798 | -46.041199 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b62df90b-6b1f-311f-95a6-f5fcbda859e1 | -11.0642 | -44.080101 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4b821b8-3150-3889-90e3-7a92086de319 | -13.7124 | -49.128201 | 2026-10-09 00:06:00 | METOP-B | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e30e4e0c-6276-32df-992e-369077c3d711 | -3.5481 | -54.686901 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f7cd64c-37fc-3f21-ba76-d1e28ee5b731 | -6.1568 | -47.9352 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45036610-132c-3554-bf74-d8a12f3e25b2 | -15.5676 | -44.509701 | 2026-10-09 00:06:00 | METOP-B | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c715f3d-7d46-3ef8-b97f-987944237f24 | -11.0557 | -44.044102 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2902f727-13c8-3b17-9ed7-3bd33ac7d3bd | -3.2524 | -54.277699 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90ecbb3a-af54-3a07-9156-2499edb80c11 | -3.5579 | -54.6847 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a17602a-d568-34d4-93bf-87877b87acc3 | -9.2704 | -45.634399 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a780bb9c-ac80-3019-88e6-3aee37a6c4c5 | -8.7228 | -45.144901 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fd232e38-cbd6-38f9-b8f5-81501ab3deae | -5.9743 | -55.346901 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61c9c1a9-b37c-3598-b824-7a5a58111f8e | -4.54 | -47.042702 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
