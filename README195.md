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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 994dcebd-8d4e-3170-b500-b25e138bb462 | -8.74971 | -69.65727 | 2024-10-02 06:27:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7846a2e-d3e3-3396-b224-0122c193cfc4 | -8.7525 | -66.61911 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba85fff2-4ad2-3dfb-9685-8bff4681a5f5 | -8.75484 | -68.91663 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfa0a7a5-48cf-3cfb-bdb1-f53f744c96b6 | -8.75558 | -68.91107 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b26d9b79-8441-3f90-879e-768727b90820 | -8.75761 | -68.91695 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aaa1a9b3-99da-3ec0-aa36-229e087ef87a | -8.75773 | -66.62392 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbfce6a4-826c-3dfb-a64d-06c8632ce430 | -8.75838 | -68.9114 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da1013c4-a455-319b-9636-4bed20c03c3b | -8.75977 | -68.91733 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70b836c6-0efd-307c-a64b-b3aa22581900 | -8.7605 | -68.91175 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4edf214-61db-31f7-9215-e5e1f46dd7f6 | -8.76399 | -66.6207 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ec56d37-b8e3-3f00-b63d-985058b33145 | -8.77026 | -66.6174 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 790290f8-7376-3095-a829-cb292f9ba533 | -8.7792 | -68.72556 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef6ff64-9473-32ea-b9a7-4b7301894ff2 | -8.7796 | -68.7227 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6759503-9b98-3c32-bdc6-a2f44bcac0f8 | -8.77994 | -68.72548 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 828364af-c44c-3653-b9bd-3e72b0ccd0f3 | -8.78031 | -68.72261 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fb33841-5dee-3ee7-974b-3e29f0f8dfa3 | -8.79054 | -68.76065 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f2c3e42-1e17-3e3a-a5bc-6eb3676eeba6 | -8.80191 | -64.25799 | 2024-10-02 06:27:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f123abe1-a8c1-3cb8-bb60-64506c746263 | -8.80266 | -64.25204 | 2024-10-02 06:27:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13143736-2c26-3089-9565-bb340533e17a | -8.82735 | -67.39008 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1383a7dc-36eb-38ce-924c-968db489531c | -8.91668 | -67.39615 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecd80a01-a726-3071-9eda-82d377e198d7 | -8.91715 | -67.39256 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8afd47e7-d468-3314-8d70-fa499e14faf4 | -8.91763 | -67.38896 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7ab4bdb-7677-36f8-986d-54b864f73030 | -8.92167 | -67.40049 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baeee629-9a89-358a-bcf6-d8ee7e8b5faa | -8.92214 | -67.39693 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbd152ac-33bb-36cd-9971-785b262b5da2 | -8.92262 | -67.39335 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c559181-e7a3-3a4d-8633-e53507b476d5 | -8.95323 | -64.36195 | 2024-10-02 06:27:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aaab4317-4072-3150-b1d0-a98632b9c459 | -8.9907 | -67.3495 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bff93a09-fbe2-3bc7-8b70-a09e7a0cc5fb | -8.99572 | -67.35391 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e1c77ac-fd74-3cd1-ba00-3c7ed100424c | -9.00043 | -71.58024 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ce1204b-c01b-31e5-bb27-d8056662bb21 | -10.11293 | -67.8932 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c511510-1cb0-3768-8497-1d62aa081a16 | -9.00047 | -67.44598 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd16be7-deb4-3f33-aa80-f7d989a9158c | -9.00096 | -71.57655 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74836e08-caab-39d9-8a4d-f679456434e4 | -9.00122 | -67.35462 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd22d5c9-e910-3cdf-8d64-620fdb339c50 | -9.01387 | -67.38606 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff46d38b-f2b5-35f8-84db-9331dccf7917 | -9.01935 | -67.38679 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf68a325-bb99-393c-b3fd-6ac45a933293 | -9.02097 | -71.5834 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43e0b7e7-1048-340e-9c07-4cc7354c6c7a | -9.02419 | -71.58269 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d094dfe1-a065-3eb6-8962-12cc3abaf7bd | -9.02509 | -71.584 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57c49ade-13fe-373c-9f6e-c69a9d8dac67 | -9.02562 | -71.58031 | 2024-10-02 06:27:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10971d51-56eb-31b0-baf7-ca594ca41714 | -9.07945 | -67.57466 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5a2758e-3afe-3f90-9e2a-18b2cd5e7e6b | -9.07991 | -67.57116 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1fda828-6123-3780-8e83-7722e251b9c7 | -9.0802 | -69.98669 | 2024-10-02 06:27:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7c3973a-92d4-313f-889a-2d566d5cad7f | -9.18378 | -68.2928 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9596bdec-a2e5-398f-a7a5-fa4f6445f950 | -9.18419 | -68.2897 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 413d8351-93cc-3a7c-a4e1-35d15f4ff19f | -9.21718 | -67.78281 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6791a36e-c286-3d4b-8c57-1dbd8e4b02c8 | -9.21914 | -67.7842 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87266165-6752-35ef-ba5b-41edeacd3d7f | -9.23777 | -68.77781 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 620cfaeb-5060-311c-b9da-ffe9773c5bc7 | -9.26108 | -67.60979 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af6ddc16-c2dc-3d02-a507-1acdb74b260e | -9.26152 | -67.60632 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 195b341c-8007-3fd3-84a0-bbdc5b53acb7 | -9.26783 | -67.60011 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e37512aa-1542-3d79-8b00-ce7a42a5a431 | -9.26993 | -68.84158 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 526fe14f-ae67-3d69-835d-43cdccbdf3c6 | -9.27032 | -68.83868 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9804c44e-60de-3b5f-8e27-b8a6b1ac5754 | -9.2719 | -67.61137 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4e5c21a-44e7-3a28-bb4d-60b9291dff8f | -9.27235 | -67.60788 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 490f287b-87c2-36f6-8ae4-2afd9aa542b9 | -9.2728 | -67.6044 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b7010f8-f2e8-32d6-b607-655ece57f8d9 | -9.27324 | -67.6009 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dba24554-6a80-3831-8a26-0c97f29143a0 | -9.27866 | -67.60168 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d5694d1-822f-3b6b-a3b3-7c9dd0fe4383 | -9.28096 | -67.83659 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 575f0182-4028-3323-af1c-dff7871526b9 | -9.28141 | -67.83321 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35a80d81-7065-35f7-9f6a-7140f5cd3dda | -9.28185 | -67.82983 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9038141b-2254-3d27-94e8-565e0b1e5740 | -9.2823 | -67.82644 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e05cc395-58fe-3213-8a36-9db5b43001dc | -9.29365 | -65.34769 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91d31ff3-3879-35d7-ae7e-a14f8b9e9e2f | -9.29428 | -65.34267 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3e1543b-3d16-3167-abe6-e4d82b1bbb3d | -9.29746 | -65.34883 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5242f683-3b8e-37f6-9e99-17517b1be670 | -9.29804 | -65.34402 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 552c7419-9125-363a-98f5-c5d3b8a0cbf1 | -9.29925 | -65.35381 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| baf0baeb-52cf-3b03-a596-91651d8fe887 | -9.29985 | -65.34909 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ad94896-a296-3701-bdb0-8070bc272e19 | -9.30044 | -65.34444 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a12172fb-67c2-3af6-9004-178bc75529be | -9.30884 | -67.66616 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfb089c8-c193-3e9e-8c63-f671e129bc85 | -9.30929 | -67.6627 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25787a63-ef0f-38e8-b07e-ea5ceaff7f37 | -9.31026 | -66.56191 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41f6da6d-6eb7-3235-8aaf-a5abc501cbfa | -9.31078 | -66.5578 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7034ecba-dc80-399b-aedb-e4c56d2b3d92 | -9.31514 | -67.66001 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e577594-7ca0-3a88-9c16-8975477041f0 | -9.33097 | -68.64991 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9079aa80-572f-3013-9546-e5d32b125aa3 | -9.35524 | -68.2068 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b56971d-63cb-3590-bab5-81b565eab7f3 | -9.36481 | -68.66658 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d822f746-374d-3e90-a36e-4a077e00be17 | -9.36751 | -67.74314 | 2024-10-02 06:27:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3c02080-61a5-3ca0-9d68-52be8910498a | -9.37006 | -68.78131 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a70edd3-0ad7-31b5-97a4-b7ff9b143f22 | -9.37537 | -68.34632 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afaf0a4a-8f20-3076-af54-dd94d99a1504 | -9.37578 | -68.34319 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1f01dcd-dbcb-3d72-a544-a6e622478fd0 | -9.37618 | -68.34003 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 859b7c3a-22a1-32e7-bb18-a3ee031e23ca | -9.38013 | -68.35018 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ed1f70e-3137-367d-9619-d7e6c09a8375 | -9.38068 | -68.70188 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f93e61a9-1be5-323f-9d3b-dab52ac2b667 | -9.38572 | -68.70257 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8249f86a-2fb9-334f-941e-5f331c4cf20d | -9.3861 | -68.69968 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fdf8bfc-b4ed-3403-a8f2-f82037ce1d69 | -9.38675 | -68.25787 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd0020bd-d42c-3f5b-ab23-a30832362077 | -9.39082 | -68.89113 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3038dbc7-b7d4-3e62-bece-e800585d8062 | -9.39153 | -68.26183 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c8467b0-1b04-334a-b627-74ae48736203 | -9.39173 | -68.89123 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97d6fb0-ccaf-3cf1-bb68-94010346c240 | -10.11337 | -67.88973 | 2024-10-02 06:27:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91dd264c-099a-3438-b6f9-617c20cbbf65 | -9.39194 | -68.25866 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b02c23-b5ad-3814-a426-f66bcfda41ea | -9.39235 | -68.25548 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0be8521f-4464-3207-862b-a0c34070d268 | -9.40137 | -68.30815 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 281dc1e4-6472-3708-b97a-d02172d1ca8f | -9.40178 | -68.30502 | 2024-10-02 06:27:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92eb7b5a-9d97-386f-a05f-a44f949acbc4 | -9.44212 | -67.15919 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02150878-99e8-3718-8d86-efb06afd6d84 | -9.44771 | -67.15999 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0480c31-3ff4-3bb3-8114-21606cf95748 | -9.44818 | -67.15627 | 2024-10-02 06:27:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eacdee4-8490-3b33-ad42-218e0712de69 | -9.45957 | -68.52435 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ce490f4-04ae-3f0f-978b-b85fc1f0f7a9 | -9.45997 | -68.5213 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f9fbbb3-e8aa-335e-abfd-726c24964c9d | -9.46428 | -68.52816 | 2024-10-02 06:27:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README196.md)
