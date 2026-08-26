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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf7a21e3-b6ab-31cc-a56f-8e81a64efe42 | -6.86312 | -56.57365 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a7640e5f-4a5d-3529-b946-7cc9feb4e9ee | -6.98951 | -59.28225 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12673389-2717-33e9-ba07-9cc716ab08f3 | -6.63292 | -58.50262 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1550292f-0746-325a-84b0-4d660dd5a6f3 | -8.22297 | -55.01096 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 826f21d2-1fac-3934-b0d5-ee6af7431cbc | -6.65121 | -58.50897 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9a562187-ab5d-3b69-9f8b-7fb89771ef57 | -6.74286 | -59.64218 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6adc0c8-54ce-3409-8552-cf7d16ea94d4 | -6.12402 | -53.74934 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c72a42d5-c4ef-3146-bbbe-dbe5e0172ae1 | -5.94797 | -57.73164 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2346f694-52c4-3d2e-be01-7a19f04e12db | -6.7964 | -59.81547 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48bb35cf-7576-369f-a90a-0a4795dba185 | -6.62681 | -58.49808 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01f1cf81-e781-35d4-aedd-bae3e3e7d271 | -3.19829 | -61.28159 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa76dc13-bff3-3008-b2db-2fdf1bad0eae | -6.26871 | -53.38497 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4bee4a03-7846-37ba-92be-c6359f96b38b | -7.0028 | -59.30571 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec268cba-27ed-3f7d-8790-ca21d014e4b9 | -6.17459 | -57.93054 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db4095f7-81ad-3195-8ad9-29d204c83147 | -3.0678 | -61.21629 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30d50c8c-96eb-365e-b10b-e56e1e22ed50 | -7.07638 | -59.22555 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f774e197-9bab-3676-8ae4-3fdbc735e726 | -6.64122 | -58.50739 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78b6f973-c36e-350e-879d-4000c599099c | -6.22971 | -55.47527 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28828781-3ab6-3984-a366-667b3c743252 | -9.02638 | -50.79012 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b31299fb-81d8-3542-a41d-df9854c6d804 | -7.05973 | -59.22581 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02fc8b89-d29a-3762-b04f-306d3b0fe7ce | -6.63789 | -58.50687 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82322db0-d5ac-391d-a843-c05bb9d1d74c | -6.14811 | -57.70353 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7028ee0e-4d45-31ce-b16e-a82f69ce7cbe | -7.38438 | -55.15205 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 47bd58b5-8f41-3506-9845-e4e57422f1e2 | -7.48222 | -55.27412 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a693580-2d23-3eb3-8075-c9832f8c6fbc | -6.12862 | -57.82864 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c35fe6c8-46e7-311f-ad99-3a47bd9cb5a1 | -6.88909 | -59.40529 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| baff4551-2ff3-3f08-9201-1c489b67dd2b | -7.47559 | -61.38049 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b9f5bb4-4dda-3724-b381-0e7a7ea608ba | -5.79167 | -57.61205 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8010a63e-3813-3351-adde-edcad40a923d | -6.18185 | -57.75283 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05d249e4-aeed-317a-82f0-de1494e30b23 | -6.1219 | -57.82756 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8aea9d6-53fe-3a08-a5fc-6340835f6921 | -3.10942 | -61.23125 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a3405c8-6495-3749-bcc2-d2b508e2050c | -6.50736 | -55.22366 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d36612e-6586-3b8e-937f-a4322995f891 | -6.8104 | -59.6852 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 907db7f1-75b2-3786-a7a4-e88253136695 | -9.03743 | -50.78762 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f736f88-f523-3b34-9c40-5dfea7fd2154 | -6.26734 | -53.36488 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be44e998-a293-3830-8207-c019eb975a06 | -6.1796 | -57.70103 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cce253ca-0187-36f5-84b3-ac1941824583 | -7.51417 | -61.38295 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 569f567b-daeb-373d-9be1-d48dd1822c3c | -6.33008 | -54.74533 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b959820b-7a1a-395b-bebb-a30256b1d484 | -8.14793 | -47.50327 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3449298e-7b35-378d-b2eb-ec43b8eabcbd | -7.02488 | -59.23095 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd95f5f6-4c77-34b1-a217-f9d799cd21fa | -7.40277 | -55.15994 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d77688a0-a3ba-35d6-9bed-7a58e0854da0 | -6.12918 | -57.82507 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2a35a6a9-7114-3652-8904-b02f4584f8d9 | -8.54736 | -54.78222 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e673f350-aff4-3d70-84f8-102e0e05c870 | -6.02842 | -58.0419 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91b0fdcf-06e1-3b20-b11a-34a563098154 | -6.71635 | -59.12896 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d94f815f-0975-366c-b4db-c43235d6396d | -6.86529 | -59.40506 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f8f6a9-318e-340e-a37f-171bad8125d3 | -6.74341 | -59.63871 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 068917a6-5ef7-39e1-b620-d92b16e7bbdb | -8.12052 | -47.46176 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 760a1a87-97e9-3b17-8c6a-ccce7f5cba11 | -8.08621 | -45.90424 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7518baf2-aebb-39b2-a8f9-dc31ee85b08b | -5.76974 | -57.55347 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8659a8-6eea-33bb-be76-17239d096e72 | -6.13401 | -59.89332 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5489a8e8-2ee6-3b4c-81ac-ab2b32c564c7 | -7.01326 | -59.23977 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 512e2bbe-e289-3e48-8c67-b17bfd621a86 | -5.77256 | -57.55759 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 627f0584-b6a8-3654-8ea0-a377810385af | -6.54581 | -58.51397 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 894722df-cc98-3b36-b1c7-50ae8cf50658 | -6.12356 | -57.81687 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b44f6517-24b6-399a-97bc-01e948a2525b | -6.99948 | -59.30518 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca7e6e63-dbd2-3402-83e2-54b4b969ec3d | -8.57626 | -54.83404 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e65133e-f93f-34f9-a8e7-9edbcd5787b9 | -6.63625 | -58.51733 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5cd558e2-e438-3d20-b1be-4c0cbf10f205 | -3.53806 | -48.18812 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a2d8c525-9d1c-36b4-a422-95d4aeea75c6 | -8.51853 | -55.35338 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 581b8900-2274-3557-80bf-327635cdb664 | -8.15943 | -54.9817 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 669c7258-00b0-3fdf-bc95-5fd1ed50ecfa | -6.63124 | -58.49162 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c22308d6-e79b-360f-b31d-e79388586e4d | -3.53865 | -48.18419 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cd91cbec-43d6-3ad4-b236-fdc6b30ca4ac | -6.14344 | -59.92012 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d12bd83d-f3bd-3984-9bfa-792e97c21386 | -7.48014 | -55.28822 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f94a3a1-7e87-323e-ac7b-283a5e642922 | -6.98896 | -59.28572 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97eb5d80-f9a7-3df6-a302-b42c8194a03b | -6.27042 | -53.37329 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f286bb90-053b-34ba-ab35-04c9bb5b99c4 | -6.13315 | -57.86579 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad017f7b-693a-32f0-9f6f-6a5256c19507 | -6.17566 | -57.70413 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3c16c40e-69dd-33d8-b8e3-a6ea7081d3b3 | -9.04171 | -50.79545 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3474068-a220-314f-9414-da1f3518ec58 | -7.52736 | -61.38897 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| bce57fec-151c-31e2-be50-5e42ec8f858c | -6.95635 | -59.08868 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06d66141-b47d-35b2-a0e3-a00b3d09cae9 | -8.60742 | -54.86067 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a242cd80-4048-3cc0-91c4-a1fe7b63e25d | -6.53731 | -56.25809 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1168a58-fcfe-39af-a5a2-22d5de69ffc8 | -6.40803 | -60.05962 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afb98f16-dcbe-3bb6-b4f3-1055692f6622 | -6.26847 | -53.35716 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f1fe061-0024-3899-8391-03cfa4920735 | -6.69701 | -58.71623 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f93b5575-1379-3d53-8aa6-6ee912f36383 | -6.12865 | -57.8505 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 800f75cf-806f-3b5b-9cd4-e15733671a39 | -6.14474 | -57.703 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cd66ad6-bae7-30a2-9476-144680e91a9e | -7.54484 | -61.36863 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de59fe08-1070-3bcf-b9a4-47d35fc1b182 | -6.144 | -59.91659 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2520604-0eaf-3d35-a48e-b951a1903dcb | -6.84594 | -59.46245 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0690b98-1626-38e8-a036-fe866e1bee3a | -3.12666 | -61.19249 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98300b01-6d86-3804-8f6f-13cc08ca1e9e | -6.99226 | -59.2649 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e2be95-3ebb-335b-b8f8-355b0c79ef50 | -6.22902 | -55.4797 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 861a86ed-4425-3b6b-8535-7eb83fefef3a | -6.88822 | -59.02452 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d455f4a-3cd6-30ef-90f6-d5b7346c6b33 | -6.54025 | -56.26269 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52840753-388f-3cfb-9fd1-13994626cf96 | -6.50258 | -53.2564 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51158ff8-380d-350c-afd3-6011e2be8d98 | -6.97953 | -59.25932 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 667f2003-ea9c-3b5d-970d-57dab2d184ad | -7.51984 | -61.39162 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6aee03a4-002d-3b8d-833f-6525aac08904 | -8.57066 | -55.27976 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4f45194-4c1f-36b9-a91f-8025cca693de | -6.77166 | -59.43987 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52afd166-552c-35c0-b789-ee949b4698dd | -9.03163 | -50.79087 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ebba04b-ab51-3513-8b34-9a3bdc87228b | -7.54201 | -61.36427 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce6a41a4-326d-3e57-84fe-171fab78e0c5 | -8.06489 | -47.52806 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2561d030-8dda-3371-8b49-df45b514818e | -6.14376 | -57.84193 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f7aafc7-934f-3ff2-9522-ae045184e984 | -6.01974 | -57.79007 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ad204c-eebd-31d6-b2ee-a818edeacb69 | -6.63347 | -58.49912 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15eb6a46-2d40-305b-a4fa-fa8289a09857 | -7.48465 | -55.28404 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3ce386e-e84e-3158-b552-de549f6ddb14 | -6.98063 | -59.25238 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README52.md)
