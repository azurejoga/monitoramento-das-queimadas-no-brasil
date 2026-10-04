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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7c01e79-52b6-3561-8310-bd5bfb26e0bc | -3.04584 | -54.23038 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 04508065-33cc-365b-9586-92adab61a833 | -3.12324 | -53.75122 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2663a7fe-8586-36a4-9111-8ea2925a91d7 | -2.81369 | -54.11892 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dfe29428-b716-3da1-85f8-807f2d9a8461 | -3.89592 | -49.69017 | 2026-10-04 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1ca2afb-c102-3d73-b44c-fb49ec877f45 | -3.18407 | -54.0977 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 45fdcbdd-93fe-3d50-8b5c-ed143a334ede | -3.04965 | -54.23099 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fe5babd8-6d06-398d-838f-048f1e9cd3f9 | -3.94298 | -49.52155 | 2026-10-04 04:55:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04eea46f-c074-3385-9e19-565ac8ca8792 | -3.07281 | -49.52897 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ced63f3-73b5-303f-bc96-7b7b0052dfcf | -0.4915 | -49.10684 | 2026-10-04 04:55:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b038369-9ced-3daa-8fd9-3eb4562f3364 | -2.04442 | -48.4999 | 2026-10-04 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da100ca6-cc69-3396-b65f-b3b04ae6f848 | -3.12388 | -53.7593 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f240747a-8597-3490-8e7e-ad768dd4307f | -3.04968 | -54.21352 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ad4f28d-014f-33f7-ab00-9a63653d72a9 | -2.77357 | -57.68688 | 2026-10-04 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b17dfa4f-ae96-3095-b9f7-b6496f99562e | -1.10598 | -54.14019 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f086cc6-a4cd-3864-9e10-4f258ca427cf | -2.81295 | -54.12352 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 391a09a7-6966-389c-bfd6-ab6f5aded63a | -1.76611 | -55.02869 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 508f780c-1331-3420-84c0-c4fbf725b604 | 0.70151 | -51.4346 | 2026-10-04 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dcd63e3-907f-3d10-bcc2-fef7a5c5e0ba | -3.64018 | -55.50258 | 2026-10-04 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e7895d-06fd-3c36-a7dd-66b26ff1cc95 | -3.17359 | -50.53866 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4cb51c7-6493-324d-8eb7-a79b0d93feed | -3.10752 | -53.73082 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 629b8a1b-1933-37c5-8f66-ce166919c48e | -3.15952 | -59.0888 | 2026-10-04 04:55:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4922fa98-5284-36f5-82dd-862275baea36 | -2.77923 | -57.68249 | 2026-10-04 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0490b5b-ce08-3773-8f75-8c63f53935b0 | -3.51297 | -54.62113 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ce9ef4e-f777-3cad-b8e7-71635bff45af | -2.95135 | -54.12936 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1f871ae-b63c-38f1-8764-9af584ea93a7 | -3.52536 | -54.61827 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16eb7030-50bf-382b-a138-025e25f03626 | -3.13065 | -53.75242 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e3ac40d-21f3-3ea9-a09e-3ade9243e709 | -2.96592 | -54.10574 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be1e54a9-45b1-3076-9951-defc3f29797a | -3.73513 | -53.424 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c084fa26-c792-383a-aa27-bbfd728ca732 | -3.36125 | -43.38718 | 2026-10-04 04:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ed9d8c9-e363-39a5-9244-a3c8b510b297 | -2.77442 | -57.68168 | 2026-10-04 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0263e0c3-faa6-342f-b0a9-fb4b7ae5ba54 | -2.82434 | -54.12537 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdcfe884-dbb4-33a5-bd3b-03f5564680f5 | -4.26385 | -46.37088 | 2026-10-04 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a0c989d0-b0af-3a64-8a3c-c12131437502 | -4.17866 | -44.26542 | 2026-10-04 04:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69d3d5b1-cc36-3fcf-b7fa-9a4494d24b21 | -5.00401 | -45.14167 | 2026-10-04 04:55:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcc8a88b-bd36-3474-a097-2bfe9d34bc28 | -2.97046 | -54.10178 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b61e25dd-03f6-352c-a7d9-a429f8105b94 | -3.01654 | -53.89204 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 126e0bd5-b893-3619-8ae5-debad6728e34 | -2.12615 | -50.25251 | 2026-10-04 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdf82928-09af-3205-b659-c2751256d40b | -2.98867 | -51.0442 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e026ecf-33c7-3cae-b5d8-3d078d5c6412 | 0.06117 | -49.9903 | 2026-10-04 04:55:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f0e740a-ba91-34d0-b3cc-41c44168339c | -2.1537 | -53.66257 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bdb48faf-d85b-33e5-9b06-cb2e55d4e3a3 | -3.04747 | -54.22739 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bab77430-0b74-339a-9f72-e51301765ca4 | -3.81024 | -50.85599 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d80a8cf-82b1-34de-9fa8-46d203d6c628 | -1.41339 | -49.26536 | 2026-10-04 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10cdefc7-89cb-3c53-b5f9-5754726ca281 | -3.18711 | -54.10294 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a223096a-a987-37ab-8da7-4b9fabafbeb7 | -2.24454 | -51.91891 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fe315f5-af0a-3313-8b8f-0f4b8e658d39 | -3.46616 | -50.10273 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 268d29eb-263c-3ed3-82bf-f7e774e70de7 | 1.94481 | -50.91465 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cfadd5c-2561-3f8e-9e22-c4c9e0d7bada | -3.70185 | -50.66488 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ead642b6-6790-3137-8b00-3b62d5ab40d1 | -4.28281 | -50.26346 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| beec1696-4094-33a7-9311-e96d26c11002 | -3.07949 | -49.53001 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b0dc280-b3f9-34f4-88c2-f74cad54be02 | -2.95952 | -54.10242 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19f1f541-abfe-3a2b-a588-7cfce5fc640c | 1.80612 | -55.5583 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 383cb09e-95bb-36ba-acef-34fc198730f0 | -4.45993 | -50.97985 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52067f90-5004-3f83-b379-36c7f6923d29 | -3.11396 | -50.27729 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17113f72-3633-35cb-ba42-3fe865d8e4da | -2.80907 | -54.09932 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9818258e-2a42-37e8-873c-7f8c577fc99e | -2.8198 | -54.12938 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e70f0653-0b35-3694-babd-c13cfb4d2e6a | -2.81072 | -54.13738 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21224f2e-4d78-3878-9ee0-e157e7b1cfab | -2.96114 | -48.70691 | 2026-10-04 04:55:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9728cd24-83c0-3eaa-b88a-e0eb4fbee930 | -3.58771 | -54.53215 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32e45322-ff29-34eb-bb12-998cc2ccd6b1 | -4.26629 | -50.75031 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d095e6b-e280-32a0-8c4e-f469b953b718 | -3.05701 | -54.16745 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b565050e-3e8c-3417-baf8-10fd800a6f11 | -3.12833 | -53.7431 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce9c4f9-1ab8-3648-a6e9-cb27b843074c | -3.30613 | -53.84034 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7971825c-e01d-3af1-8dda-0822316fa086 | -3.07598 | -51.2821 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20c53b2b-d262-3482-9101-d429436c4bc5 | 2.09945 | -50.74028 | 2026-10-04 04:55:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77c44827-e1c5-368b-bb72-c1eebd1ac16a | -3.10621 | -50.28316 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcba255b-124a-3302-a3d2-669891812f45 | -4.27616 | -49.9816 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dcdbc88-dbba-3967-a99d-b4a9848a4327 | -2.75465 | -51.54945 | 2026-10-04 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33560a8a-c6d8-3ded-ad29-9c21f61e72c7 | -2.58057 | -51.87278 | 2026-10-04 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 13f0a130-d84c-310e-b2b0-461d5a603ccc | -1.33085 | -54.66368 | 2026-10-04 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 967d13b6-8f11-3530-98af-8550a4c05eb1 | -3.0734 | -49.54692 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 943fda71-3360-35ee-8176-c524840c3fce | -3.06109 | -54.16198 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e52d1995-916c-3c73-86bc-0add5161f33c | -3.1311 | -53.7257 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 791d5104-0405-3282-bcde-9e3547186b14 | -3.13702 | -53.72572 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 894ec561-5916-377c-b6bd-3f7961677540 | -2.7939 | -54.09689 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdecf238-74bc-3c18-80b2-1dd48e81d732 | -3.7035 | -50.65448 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b5ece5b-9575-30b9-86d6-50b5737f2516 | -3.17117 | -54.08157 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ce80df6-6e5c-31c5-b542-34a973b0cc80 | -2.96213 | -54.10514 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cac3a260-5277-3821-bd47-83da7224db12 | -2.96709 | -54.10364 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19e17dfa-f206-3b86-b6a1-5532db4d3226 | -3.50491 | -52.95862 | 2026-10-04 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f84655a-7df4-3806-8b5a-f149b95e36ae | -3.00752 | -53.87696 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c97f49-7f5a-3d54-9a36-6f255b40bce6 | -3.05395 | -54.16223 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b476b2d9-cad2-3c7a-8e81-b986833ec663 | -2.7962 | -54.10668 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3dbb1890-70e9-3621-8361-58fff49d42fa | -3.13479 | -53.7263 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c28ceb5b-9940-3cfb-831b-01fd075facd5 | -2.80305 | -54.11247 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b5137e2-8e4e-3c65-98fa-ea7335e03b1a | -3.51605 | -54.60198 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe4b5ca6-6f6a-3a45-aea1-04e6571d68b4 | -3.725 | -54.21354 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 259d7a17-e7fc-3aca-a1e8-fdb5bb5f3b55 | -4.28946 | -50.2645 | 2026-10-04 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ae7276b1-7f38-36bb-a264-517a45138a67 | -2.97574 | -54.09327 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa3ccbb6-5dc0-3ea2-873d-e4d1d45be905 | -3.00655 | -53.87891 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a956a4fd-18d1-3eba-80ee-4f2a3c0c29ab | -3.08063 | -49.54448 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b62e908-fff1-3da3-8af4-7da1f7ab4262 | -5.12407 | -42.4069 | 2026-10-04 04:55:00 | NPP-375D | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9e37304-a539-3067-9c26-b5b1fa3fac3d | -3.13272 | -53.73935 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1923512-d29b-3f7d-898c-0238de24a923 | -2.96403 | -54.09845 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac32e7e4-c052-3825-bf60-70b607c76a09 | -3.51528 | -54.60675 | 2026-10-04 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b0d6cac-9abd-3c01-8df7-249ab86c5c88 | -2.92777 | -54.10665 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c8fff0d-2f76-38cb-b196-a3cbc2950c96 | -2.9003 | -49.40215 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32de6f4b-6e2e-3c7b-b053-ecc20bce3ec3 | -3.06449 | -49.53838 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 857da8c2-0637-38b7-9d91-876d7f54b504 | -3.29128 | -53.83794 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5723d5c5-24f8-3fb3-b5f1-851534288910 | -2.79011 | -54.09629 | 2026-10-04 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README43.md)
