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

## Dados Diários - Página 220

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceee20b1-0c62-3b23-8504-eff3cdaa06d7 | -8.98572 | -45.93918 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| db72dde7-1bd2-3713-a04f-38f02f2a17a2 | -5.336 | -48.55636 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 0970c7a3-3e1c-3a5c-a1b3-633f28bb8469 | -6.26915 | -52.84384 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0c230712-ce13-3fe3-b60b-d91f829dc091 | -5.16741 | -45.32167 | 2026-10-07 16:37:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| df525041-4c54-3511-a20c-9551608f9b6d | -7.8687 | -54.96218 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 84dff5b6-ba69-3831-8a4e-ca553884779c | -3.19849 | -42.61353 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 2586b677-6c81-3d79-b452-024ae5a23271 | -15.63893 | -41.69475 | 2026-10-07 16:37:00 | NPP-375 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 8cac2fd0-f477-3e1c-b778-02a55c42bd23 | -4.62695 | -48.85738 | 2026-10-07 16:37:00 | NPP-375 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 909d5839-6151-3085-b1d2-a503397b6a33 | -7.3921 | -38.62983 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 1de42ebc-03ec-3976-9edf-acfbd047cf9d | -11.2048 | -49.42341 | 2026-10-07 16:37:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c82bfb7c-8e2c-3694-a07d-75020bd9423e | -14.7036 | -41.26883 | 2026-10-07 16:37:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b517b122-120f-3c0c-b7e4-957a5c3f7444 | -7.00136 | -44.05087 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 88210f4c-aaa6-35bd-8ae0-c98efd0bb211 | -6.8466 | -41.77348 | 2026-10-07 16:37:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 4b87ddfc-1c90-3eb5-b986-ea87bb869e6b | -3.58474 | -45.47884 | 2026-10-07 16:37:00 | NPP-375 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bf12d7a3-56f8-353e-90eb-4f0cff853ac5 | -8.74486 | -44.20335 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09206e94-1948-3bd8-9b66-b9c6a86390d5 | -17.02751 | -45.92233 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6ecfa59b-81c0-3d5c-a6e5-fb66fd98f619 | -8.21289 | -46.36024 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 22fc624c-1a5d-309a-b3cf-e07e33a11dd2 | -5.83345 | -53.53177 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ac9c468b-8668-3a0d-8f9a-ce4be53735db | -6.6415 | -43.77454 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba3be6a1-c69b-32d8-9af5-f60eb2594d7a | -7.20702 | -46.56526 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 37792c4d-3964-3f0a-9ae8-c955cf599896 | -3.70153 | -44.88915 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 988e1316-e77d-39c2-9cf7-0e81517e8425 | -7.03493 | -45.42459 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7cc9277f-0881-3fb8-bf79-a4e657d74a84 | -3.049 | -53.91615 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0d99cd25-9a69-3ad4-8e83-b1e8ce58400c | 1.75976 | -55.56234 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 605417ce-ee66-3827-b88e-1a92bef119fd | -3.50606 | -54.65811 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 606443c1-84fd-39da-9df0-7f2faaac4fa8 | -3.46947 | -50.09221 | 2026-10-07 16:39:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9850f3e5-3859-30ac-89e2-87f2ac6e2ce3 | -3.27154 | -50.41098 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fecb5f1-fdc5-36a1-9f14-b2f25ab029ce | -3.02824 | -54.23405 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e895db24-2708-3c20-954f-5737ba4fbba5 | -1.83476 | -55.04213 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 53a5b126-6de1-381b-9c75-7181162af510 | -3.35773 | -50.47375 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ffe2160-1663-3f96-85fa-3c3c2c812597 | -0.90873 | -47.45722 | 2026-10-07 16:39:00 | NPP-375 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 13ecc743-7f57-372d-962a-eb8d1b43a931 | -0.83619 | -49.25904 | 2026-10-07 16:39:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a171cbf8-d747-3a1b-b17d-e8ac18939bda | -3.18045 | -50.55454 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 85cf96fe-05f1-31e4-80a6-714ec08dfaf1 | -0.81808 | -49.1141 | 2026-10-07 16:39:00 | NPP-375 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8bd0b84-be85-3382-a38a-4c066a256e8f | -2.25158 | -55.0569 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dc046197-d9e6-3e5e-9b69-abc386db0d48 | -3.10575 | -50.25608 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 00ede3fe-cb6f-3241-ba48-3db70f8a42be | -3.04072 | -53.93431 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4012a53c-4d97-362c-8499-9b924de0cc90 | -1.10681 | -52.25942 | 2026-10-07 16:39:00 | NPP-375 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| efb6a629-2475-31a5-b99d-5a11f604a4f6 | -0.59174 | -49.42194 | 2026-10-07 16:39:00 | NPP-375 | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| cdf754e8-09bb-3e2e-a5e5-bcb9cf935d77 | -3.37573 | -54.11153 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8b2b49ab-412f-3c62-a3f1-80ae3521c73a | -1.15263 | -54.09972 | 2026-10-07 16:39:00 | NPP-375 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cafc70f2-be4d-374d-9f36-55384976ee23 | 1.99102 | -55.87738 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99eab90c-3230-398f-b2ef-2ce3ce0355d0 | -4.13308 | -54.90444 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4cc9f30a-fb3c-3322-98a7-d9b2a41184ce | 2.10311 | -50.96178 | 2026-10-07 16:39:00 | NPP-375 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 219f33c4-9aa4-371e-8e30-d2398f286625 | -3.29877 | -53.86548 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 15a11dbc-f6fc-3480-ab29-ed5c8bec3921 | -3.52752 | -54.64695 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| acefd1c3-0acc-34d4-85f2-a581d1250c39 | -1.27656 | -55.84542 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0391c6cc-9ad7-37c7-87a1-a6c9be90d10c | 1.19618 | -51.29176 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 595265fd-457f-35bd-b5cf-719cd90d8e8d | -2.46677 | -56.0916 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7ebc760a-976a-30f0-b768-617d4967703e | -2.93982 | -54.16181 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| fd6a635c-fc5c-34fb-a854-82f9d3b97de3 | -3.0862 | -54.28568 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| dce4b77b-547f-3de3-b881-faaeccaf5fe3 | -2.50187 | -56.12103 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5ddadaf1-37fc-3355-9211-356a46d814cd | -4.098 | -53.98866 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| feb15709-fed2-3bda-bad1-145fc3d68651 | -4.09876 | -53.99096 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e4396e83-7260-30c2-b0d1-0aaf3e4628f4 | -4.92162 | -55.86019 | 2026-10-07 16:39:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c00012aa-06da-3872-b522-b53a3846183c | 1.76663 | -55.58962 | 2026-10-07 16:39:00 | NPP-375 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 33f00573-57d0-3a9a-aea7-0bb0849f893c | -3.04371 | -54.14553 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 522ad3f5-034a-3935-916e-dc013972d10d | -2.77946 | -56.50097 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cacf8462-8d45-3a62-baa5-33c7d2c8d413 | -3.35028 | -51.62098 | 2026-10-07 16:39:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ebbb6026-c559-305c-9bed-5100b7eb5b33 | -3.48362 | -54.62294 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db18ddbe-cd96-30e8-8af9-1b05ee08c096 | -2.42449 | -56.53436 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 00e91b96-a853-316c-9006-05616155f397 | -2.60084 | -57.57161 | 2026-10-07 16:39:00 | NPP-375 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8112ac56-b44a-30e0-bb9e-d09df4b52ac6 | -3.84283 | -55.98992 | 2026-10-07 16:39:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9b5b36ac-ddc5-3651-ab27-2cc1b43ea882 | 2.00592 | -55.85655 | 2026-10-07 16:39:00 | NPP-375 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| bf9bd892-0d91-365e-8e23-1c2316370054 | 2.23995 | -50.82927 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c8dd060a-1331-396d-9062-6c2afbedaa42 | -2.90039 | -54.02207 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cbd0f281-eb44-317f-9854-5f48a65bff9e | -3.26732 | -50.41159 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76bb4f80-3733-3aaa-b152-94e6c4cd1808 | -3.26446 | -54.65989 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| abd39490-0883-30e2-8c70-4c479aa9d2d6 | -3.53985 | -54.63732 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 137546ec-a2d9-3615-bcb9-b23a060ad808 | -1.60455 | -48.28459 | 2026-10-07 16:39:00 | NPP-375 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 17f004cc-b5c9-3d72-a853-3f8410b20c1a | 1.3465 | -50.8602 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a577077a-115f-3359-be6e-806a7ffd6c09 | 2.55359 | -51.10522 | 2026-10-07 16:39:00 | NPP-375 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| da874cde-91f8-34bb-a73b-8ef9133d75ff | -3.55943 | -54.4931 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55d9331a-c35d-34a1-a8ba-3316e2e2e592 | 1.46756 | -50.75322 | 2026-10-07 16:39:00 | NPP-375 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b8a15b46-66bf-350d-9c5d-566092497246 | -4.09279 | -52.06694 | 2026-10-07 16:39:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 97ec2ce9-aee3-3c85-842a-9a2a920601f0 | 0.38284 | -51.14203 | 2026-10-07 16:39:00 | NPP-375 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4ba4e7c6-85d9-33e4-9f00-c1264019a63a | -4.56621 | -54.95612 | 2026-10-07 16:39:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5f116808-b797-3163-8074-4067df3a6d8a | -2.02242 | -47.55292 | 2026-10-07 16:39:00 | NPP-375 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 391fb01d-eaae-3256-8979-d920ff2992a1 | -3.17851 | -50.571 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 94228095-7042-3d59-939b-1f9ef97ba810 | -3.58859 | -54.30419 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 60bfed71-48f7-356e-aa83-2e6ffafa685a | -2.99562 | -54.05234 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6c580dc4-7329-3972-90c5-717b76f9efed | -3.1762 | -50.55517 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e5fa2eeb-bc42-325f-9dd9-1f471323a408 | -3.08319 | -54.30178 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2110df3a-ede9-3347-86b0-cb94bda86b9f | -3.18779 | -50.54544 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b31b871e-5632-3d05-90b0-8054bf96a31b | -2.52292 | -58.09859 | 2026-10-07 16:39:00 | NPP-375 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 421bbcdc-4160-3d35-8d76-a1ad65936ae6 | -2.70831 | -56.54202 | 2026-10-07 16:39:00 | NPP-375 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d9ab864f-c203-3960-97c3-8ed33d8d4569 | -3.30126 | -54.03076 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c0f11d2e-d26c-382b-9fe4-f32cd6235e9a | -3.27496 | -50.43429 | 2026-10-07 16:39:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ca2fee0d-5ec9-36e1-8859-ddceb8f94910 | -2.98515 | -54.13079 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| c90eb271-ecd2-31cf-bebd-d00839e8ac47 | -2.46748 | -56.09626 | 2026-10-07 16:39:00 | NPP-375 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 355f6c58-9617-3e36-8444-6ab9cd8cf3df | -3.04977 | -57.519 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| af39174c-df1d-3c0f-913a-212451424b90 | -3.06612 | -54.37481 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2a083ce1-eea6-37a5-acb0-c6a5d653c25c | -2.93631 | -54.11398 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b20b7b1-f621-37f6-833e-580894271e06 | -1.75174 | -55.12441 | 2026-10-07 16:39:00 | NPP-375 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4944cd25-cfd3-3af7-8045-b7a56bbcd1fb | -2.93538 | -54.1695 | 2026-10-07 16:39:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b221f8cf-a918-382c-ae39-25fe2c6edc80 | -3.1092 | -53.77306 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ccdebe04-34ea-3fd3-a070-fd877aa55960 | -3.08176 | -54.29369 | 2026-10-07 16:39:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| cddab48e-4ecc-3651-81c2-5a3b85ac8403 | -3.31521 | -57.9907 | 2026-10-07 16:39:00 | NPP-375 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5fc37e43-658e-3d98-bcfd-9459034e3adb | -3.52243 | -54.65162 | 2026-10-07 16:39:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d02f2d1a-d599-349b-b888-be0a9e903c5d | -4.1546 | -54.03032 | 2026-10-07 16:39:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README221.md)
