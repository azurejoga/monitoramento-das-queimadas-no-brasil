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

## Dados Diários - Página 198

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 571b3f8c-1632-39d9-a792-ae194ce2c789 | -3.57474 | -54.35731 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7200a5f5-b931-3f8a-8350-90ad3c58779e | -3.29059 | -54.00508 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0930172c-ea74-35ef-aa56-a48fc4171214 | -3.42879 | -58.59881 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d73776da-9b01-3cf1-b326-893ed0747d6e | -3.28037 | -54.07184 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fa42f87-29f8-3e32-b5f9-2617bed1fc06 | -4.75374 | -55.65976 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8211507a-e12a-32b9-b0dd-50235459a23c | -3.0958 | -53.73107 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b9703f7-bfc1-34cf-8fe9-09335be2386b | -3.19108 | -50.56976 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 979c6a3f-f222-3eb7-b688-272c96def06a | -2.47539 | -56.0993 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b429a9e-9f56-39eb-a2d2-145eaf552a45 | -3.2934 | -54.02253 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ba4e509-3a06-3ab3-bcc3-f533f16b511a | -2.12273 | -54.80568 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ac9218d-95a6-31fd-a94f-bcd1569e029c | -4.5757 | -54.95805 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0f85d3b-edf4-311b-ae4c-1b5d12404f66 | -6.98576 | -59.10793 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea00094-004c-3c69-97ee-9e1574dcefed | -3.05948 | -54.21379 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78c4152c-f51b-36bf-b24f-9f5a35304170 | -3.51432 | -59.3218 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39a2aba8-d9c6-3146-aaea-fe12a2fe9587 | -3.56023 | -59.4788 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f574a982-6f52-34c0-9526-9df240205ebb | -3.29824 | -54.02665 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa4f540a-80e7-3aa4-8d7f-4586ae259de3 | -3.59017 | -54.57759 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3d42def-26fd-3ac2-80ac-88e7254c271e | -2.77652 | -54.06274 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48b7eb99-964b-3e8f-90ad-85f82aa99e37 | -3.29239 | -54.08743 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fc1265d-88a6-3db1-983c-a8a1304bf54a | -3.31327 | -54.05674 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42de27ee-ade6-3edc-be4a-597076397284 | -3.29436 | -54.03661 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f5a4d1a-9738-3d45-b92f-0ec8e0e91f39 | -3.26456 | -54.03218 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f57e699b-1499-3535-a1fb-de42b84853d6 | -3.79306 | -59.37203 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca238b5-2d43-3487-ab12-c5274b8458f7 | -3.29008 | -54.00841 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8dcec58-1e70-3834-a86f-40156c0c3dcf | -2.77889 | -54.08318 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4cc79c8-6737-35b5-9457-4811dbe141b8 | -4.92507 | -55.8534 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e89eda62-9dce-3e90-bd4e-b19720d82137 | -4.35592 | -59.94875 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b1a8899-9a20-3e3f-95ee-e68a32b4213e | -3.63364 | -58.94106 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d8cca7a-179f-3bb5-83d0-3c9a8580371b | -3.09195 | -53.71973 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b502274-140e-37f2-8752-49ac7c422b3b | -2.77359 | -54.08241 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3992c8d2-3e08-3909-8518-d03d14e8bb89 | -3.67121 | -61.15672 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd5e5a3c-5df8-3397-9973-d1d4999dcdd2 | -2.78035 | -54.07338 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bbedee6-ad8b-3a2a-8c5a-0020b636b8c2 | -3.47894 | -50.09306 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97347cbf-0f39-39aa-9428-0f8f096e5d0c | -3.29781 | -54.01294 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d4c4fd0-66f5-3d36-9638-85a997467f32 | -3.29532 | -61.00845 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3fb44b7-6e78-3e18-bb3a-49d73d3d6f66 | -3.10561 | -54.19363 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cb019b5c-f761-35bc-b375-6a64bd2a727f | -3.2827 | -54.07917 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d05c23ff-b289-3c23-a164-94aceb17c056 | -2.93484 | -54.15366 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 962654c0-6b42-39d6-bac4-222eb6ffef2b | -3.04991 | -53.9246 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e89a09ea-1d97-38c4-adbc-6ef0ba53ba39 | -3.84911 | -55.98776 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd1d7b99-91ff-31af-bf9c-0620d0a296f5 | -2.87346 | -54.88652 | 2026-10-08 05:42:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c753d75-e448-3dc1-9ba5-2494667449f3 | -2.50246 | -56.13679 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 330301c7-bf4b-3762-8356-a7394cc1de47 | -3.11049 | -54.16114 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 964cddbc-7574-3a26-9958-57bee71572e3 | -3.04804 | -54.15183 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72141796-f5c7-3490-868b-7f891c25487b | -7.23077 | -55.12154 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8397165-3972-3f9e-9d68-dd438b280f64 | -2.50254 | -58.07433 | 2026-10-08 05:42:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 826153e2-5f18-39ca-883a-9e2f2605d633 | -3.47339 | -59.56284 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 057bf531-669b-3ae3-bd8f-a6e2cdf0ffc3 | -2.94472 | -54.15616 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66d15eb2-479d-3461-8e91-2843634f83aa | -3.44793 | -59.82508 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d9dcc4b-a52e-30d1-b32c-3c41a4cc85b0 | -1.83931 | -59.95829 | 2026-10-08 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba3e81d-6fa7-3a6b-bb75-d7dd201159aa | -3.38795 | -56.93271 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bb5c489-599f-3bb0-9616-cc6340a87bc9 | -3.31041 | -54.03905 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15b520a7-b1d1-35af-95eb-f6e2b439a3c8 | -6.99624 | -59.12014 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927d9cbe-ddf6-3be3-a352-837aa8bde944 | -3.95824 | -56.12547 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fadfab6-3f90-38f7-a128-aa8bd73e2819 | -1.8257 | -54.9362 | 2026-10-08 05:42:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18119cc8-fd3d-3eac-a75e-5d07dc55db48 | -3.11774 | -56.66314 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6e85869-d2ad-3507-8570-82a5f4f97885 | -3.57347 | -54.65403 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51b5ed88-99dd-3a7b-af88-8011993d6486 | -3.02071 | -53.89936 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddf6b906-5a56-3bcd-8fcb-9d9df587fcee | -3.53422 | -54.67038 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3fb7ab5-b88b-3263-8ca2-e93e3764a6b0 | -3.10192 | -53.76397 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c0d1854-86a4-3b75-a951-f1c84abf98ab | -1.79787 | -60.29212 | 2026-10-08 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 024f6cdc-5b0f-34dd-98a4-b73d64529c3f | -3.59114 | -54.57111 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac88c59a-df46-3d56-8897-997583b24736 | -4.11747 | -59.87381 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b894c4ed-e99c-3f53-80f6-371852ffe1fe | -3.26979 | -51.07521 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57bfeb80-6a66-3855-9cb9-3d5ddc442c38 | -3.56498 | -59.49779 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afbdf02d-ce54-35cc-a63e-7576f82b37c4 | -3.14754 | -53.72788 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba0c5d69-96c7-3bbc-af47-b9aebc7633a8 | -3.29029 | -54.04278 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1be3908-9880-3cf6-b734-d0bc3462c753 | -2.3253 | -60.06523 | 2026-10-08 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99692368-360b-36a4-ad19-dc8a80953ad0 | -3.82431 | -55.46742 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74577b3e-836d-3074-9387-98147c58d9cd | -3.26159 | -54.05175 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0973591a-160e-3674-8e55-4e2cd61ef874 | -3.01176 | -54.06924 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23765089-2aac-3498-be4b-a8e866392321 | -3.02542 | -53.94148 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64295239-8d74-3949-8f75-e174d9b9c15a | -2.58237 | -56.16571 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de49680d-d5f1-3ab8-b9f7-8bdc49c510bc | -3.07911 | -54.26282 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b1cdba4-ea63-318d-b1d1-5bc395e91ca6 | -3.99303 | -56.26124 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07481564-5d8c-3822-99d5-1905839a7c3a | -3.82347 | -59.00198 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12603e0d-4f50-3ec0-ad42-43edc381fac1 | -2.84796 | -54.12685 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95885deb-3f5d-3c23-b2be-c489e804ce74 | -5.70321 | -53.49889 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82c408d4-8883-39e9-aa43-9b9d746aeac0 | -2.98617 | -54.05853 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26660ba8-1311-3425-8432-b45e7e6e561b | -3.58806 | -54.66212 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 889ea559-6727-3ee5-b636-305994614e8f | -3.56126 | -59.49722 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e0b26ac-f92f-35d3-95a7-bf8b0a7def15 | -3.42127 | -59.56609 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504475a0-e782-366d-bc3a-d477a3bef470 | -3.2679 | -54.04615 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a3a9e77-4e34-323a-a88c-ce8a9e5fbce0 | -2.76013 | -54.10023 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 002c636d-d3a3-32fe-8e04-10c5240046b5 | -3.27703 | -54.05798 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab9582d1-16d8-3115-b65b-ac22b54c76fe | -2.86816 | -54.16655 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bb4672e-69f4-386b-a278-c8a0580ab133 | -4.30785 | -50.7848 | 2026-10-08 05:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fff64c8b-afb8-32d5-9281-e25f09784f80 | -8.61546 | -67.05707 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c3cb39b-af03-398a-8845-4acf21685738 | -9.05703 | -65.48892 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7eea7793-45f0-3125-bc98-32cd059f0fb9 | -11.97595 | -57.58092 | 2026-10-08 05:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f87db915-1e22-31e5-80db-b349b4ff84c2 | -9.47246 | -64.35417 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a2ab6bf-5ddb-3ec2-b465-865bd6c46863 | -9.48847 | -64.36031 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a67ff97-1ae4-35a3-9d66-2f9d9579f1a9 | -9.05965 | -65.93022 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 28a58843-a718-3973-b4d5-8f8d3ccec022 | -8.62353 | -67.02991 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 2921a335-cb41-3c9b-99c6-0bded299799c | -9.18934 | -66.01488 | 2026-10-08 05:44:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e35bae0d-128a-3878-9dc4-b31850b9dbec | -9.80751 | -65.00506 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ce12cb-a925-3f7e-a96a-efd4b0450711 | -8.65357 | -67.1767 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6b92ddbe-3e39-3807-af71-fe07aec03a29 | -9.48405 | -64.36674 | 2026-10-08 05:44:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc56aa59-a342-3853-8c8d-ef24982a03e6 | -8.86254 | -67.44785 | 2026-10-08 05:44:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0271a86c-1cf8-3b95-b26b-c3205266947b | -11.75656 | -61.06133 | 2026-10-08 05:44:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |


[Clique aqui para ver as próximas entradas](README199.md)
