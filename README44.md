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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e80ad04-609c-33ea-8904-a151c875f2ed | -1.60695 | -52.22997 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a47c85d4-385a-3474-b37a-3a38f2275098 | -1.53715 | -60.33024 | 2024-11-19 05:08:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eaff55dd-babb-3432-a267-dba30e91065d | -2.19916 | -53.66471 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa7b932-966b-3dbb-a4dd-00c55d68ecbd | -4.54233 | -48.01292 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42af85d5-92fa-3313-b36f-c935ad054543 | -4.55468 | -48.00185 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6378918-7817-3991-bdca-beffdf14e88c | -3.31265 | -54.17714 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5d36cb3-64db-31e2-807e-7c501130629a | -5.71868 | -44.81104 | 2024-11-19 05:08:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c870197-c70d-3570-b87a-64a473d0bd56 | -4.39243 | -47.76478 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57cc3a37-491a-3f20-b85c-d830d16053d4 | -4.39096 | -47.77459 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cd4306e-e599-3390-b039-9cf566d12d08 | -1.51232 | -52.09093 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d53d004b-905f-37b3-ab71-0f733a68ba1f | -1.43899 | -53.38504 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12760689-121c-39c2-8b4a-e1e7f138630d | -1.13588 | -52.10802 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba1d95df-cd9d-3d54-9e5b-2491f578e957 | -3.22001 | -53.02639 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c05ab09-ff05-357f-ba73-ee24c35a15e1 | -4.38612 | -47.77061 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d548519-455d-3653-b611-b2896cc45654 | 1.18842 | -60.22338 | 2024-11-19 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ec29ac1-59ba-3783-b65b-c1c4a25fc562 | -2.60368 | -51.79903 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abf4104c-dcf5-3ac0-8d08-02c28029447a | -0.93784 | -51.71866 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e2fc31-51a5-359f-aed7-a55f053e9ed8 | -0.12333 | -51.42747 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73e944e0-bcf5-3fe8-880b-40a3883a76b1 | -3.55464 | -51.53463 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8833ad15-6d7a-30a0-bad8-b45e5a2401b0 | -3.06405 | -54.40408 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44263a13-bbc0-3044-a1fc-4e53e4862616 | -2.58132 | -51.92165 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2aeda3c-87bf-32bc-a717-60c66cede92b | -3.77383 | -52.40775 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c96079a-c704-3f67-b261-60ad3e890cbf | -2.3184 | -45.65072 | 2024-11-19 05:08:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bd4abe0-2b07-3038-8412-60ac87109e6e | -4.98905 | -44.33383 | 2024-11-19 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12fcfe28-97dc-3a5e-9f68-cb4444d7ce41 | -1.21176 | -51.78763 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66f2bb31-d4ee-3927-bcd3-adf716558210 | -1.90162 | -53.33283 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e990ec34-2e22-3acb-b060-46922d20a418 | -0.34134 | -51.46598 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15baad95-a5aa-36eb-bb24-d6b8885ae7f8 | -3.7244 | -52.44839 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6538240c-129e-3187-9cb4-2e740dad4e92 | -3.05972 | -51.32924 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ff5486c-de44-3bf3-aa92-e4e933eb2dbb | -2.82345 | -54.01059 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d43de182-1216-3859-9688-e054e328ef16 | -3.85144 | -50.99393 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42db9ba9-dc17-3737-a37e-dcf1c5e6b81a | -4.57811 | -48.02459 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2a50a61-0be8-3ad4-bc7a-0dd7ea0bca58 | -2.95484 | -53.72199 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18b17b7d-fa55-33d9-8d00-ed1eec0a9456 | -1.00125 | -47.99882 | 2024-11-19 05:08:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 292f6927-c505-3f36-8799-e256d30009ac | -2.76718 | -52.60607 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1fac276-dd4c-3c6b-b383-3e6ef6815dc1 | -4.57856 | -48.02146 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e49f5a78-efbd-35b4-a3bd-fd69d29d4c6b | -2.73455 | -54.11559 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72a58147-890d-30a9-ae61-8d69b77f4be8 | -2.60105 | -51.79692 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d62d47fb-0235-33b1-ac00-72f1b6a07534 | -3.76927 | -52.41181 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3905f9f1-f02a-37dd-81b9-edb8baf79399 | -1.21948 | -51.78882 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b7452e1-374c-3369-a650-5146c3922454 | -1.34721 | -55.44113 | 2024-11-19 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 485ee163-1b35-342c-83aa-45b2e6e36558 | -2.43326 | -54.61564 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d68ae9eb-1c2d-347b-a834-63c4d05e5d22 | -4.3433 | -50.45783 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8147d61-52df-39fe-9e30-b66d4b89769f | -2.5883 | -51.72339 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b5ab42e-84c7-36b2-885f-85f4c276badc | -4.99575 | -44.33468 | 2024-11-19 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d84c71c-a8dc-3f3d-94b8-fe5697b6c082 | -3.86794 | -51.16858 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 261f4040-0ec6-3769-a818-757909db5c39 | -2.54252 | -47.3357 | 2024-11-19 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d3a4746-d293-38b9-8551-96e0cf42a288 | -4.38226 | -47.76005 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5039a3ce-b983-3d17-b35a-5b4a20106b1a | -0.03493 | -51.12347 | 2024-11-19 05:08:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 909b44f1-8352-3f2c-a8c0-7dea172cac30 | -3.34394 | -45.35826 | 2024-11-19 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 286ff1b5-f443-3555-bb4a-e28f7acd2d4a | -3.32184 | -52.71272 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a1d022e-e22c-3302-9b2d-e0a81ed59c22 | -0.94868 | -51.72521 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3b62690-6bee-3e0a-8979-c8d08c26b6c3 | -2.7427 | -54.10903 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a07c7edf-feec-3cef-8d72-167b8b1032fe | -3.00426 | -51.44852 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fb82371-9aa2-3b1a-8945-deacf6b82c7b | -0.12258 | -51.4323 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9c1fd35-4ce9-3c63-8129-4403ca44e411 | -4.55945 | -48.00583 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7570d60a-6996-3f75-b187-68472f6b08c5 | -2.71851 | -51.81154 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d7082a0-72b5-3f34-80d3-427d92d47ae8 | -3.50362 | -51.01829 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe017b1c-09cd-36ef-9f50-577ea92ae88e | -4.05618 | -50.00046 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69249ce2-0930-336c-bcbe-b58075be1027 | -1.21833 | -51.74454 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0d309ad-1c95-3b3d-b6e5-4b6d1c189812 | -2.73396 | -54.1194 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8b9668c-9142-356a-adbc-c02c23175a02 | -4.39578 | -47.76816 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87c3ffc9-fa3f-3ef2-b15d-e9a7b0d51c42 | -3.33712 | -45.36194 | 2024-11-19 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 068be3ed-53b9-3356-bd6b-2a1036dbee50 | -2.01938 | -52.07548 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 599f046a-6874-3616-8632-3965ecdd33dd | -3.71167 | -51.84169 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4b8e743-a5e4-39ed-9cc1-0ddba4ed93be | -4.5847 | -48.0159 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f9ea292-0201-3fd4-afcf-ccc79fe33405 | -0.8577 | -51.86874 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95774a75-93e8-375e-bae0-9cbd4db7662c | -3.69122 | -51.56587 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c14bee47-bbae-33ee-b3f1-d7bbc0313365 | -3.50782 | -51.01891 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a98d332-4e08-3698-b637-9cbecc8394e4 | -1.42377 | -51.10078 | 2024-11-19 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8f02800-8771-3669-9e8c-56ac6cf1a98a | -1.06394 | -52.39477 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc7cbb5b-a1e4-3b1c-93b2-3b1540a058b8 | -1.1397 | -51.68105 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0771da8-48a2-3c11-9bfc-de3d9edc2adf | -3.56866 | -51.44176 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d802e081-5bee-3ec7-9e14-2ac3f6b75667 | -0.25016 | -48.52418 | 2024-11-19 05:08:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22df0c88-17fe-3480-80c8-dc5a5d3eff43 | -2.5919 | -47.47651 | 2024-11-19 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85e7266b-3ced-33fc-abaa-203872dc0c49 | -1.3981 | -52.95161 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f71b887-d28d-3343-884e-dcf4a6e8b7b8 | -2.58118 | -51.71716 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a133c67f-a9a5-3aef-b121-a015226cd1c7 | -1.37984 | -52.07965 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7e6175f-3b07-3062-8d07-20cd6d67bc11 | -2.93934 | -53.88771 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b7f66dc-754f-3ba8-89f8-9a43e53ba922 | -1.39678 | -51.98949 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f6d8fbc0-8b69-361a-a50f-17dad5f89868 | -3.06485 | -53.28273 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55509a0f-4843-3d21-90e6-d0eb5adb1ced | -0.91101 | -51.73893 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034a5f14-72b5-382a-865d-494f40841ace | -3.79661 | -50.25494 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ead7c7a1-aefd-3ce9-a956-f3692b05c3c1 | -4.11038 | -51.04815 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc4c6268-9523-3e06-ba38-4f51b5bf37e6 | -3.04386 | -49.46196 | 2024-11-19 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9c37f66-3c05-3baf-b696-b0517c8a9ff5 | -3.31384 | -54.16956 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1dcd02e8-582f-37db-96bc-1ae04aef6693 | -2.84913 | -54.00662 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7e73f6a-b714-3b30-9363-1d6a5d62b740 | -3.77671 | -51.9934 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bad1f5ac-8c41-3c6d-b729-5680b7865bd2 | -6.05442 | -44.04927 | 2024-11-19 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9530f517-7e97-3610-a0bc-cca7d209cd5e | -1.40093 | -52.61793 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86eb96a9-f48b-37ed-8fb0-a94f2c5a8cfc | -2.75005 | -54.0158 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88e8d347-fc3c-3fe4-a329-e10e43738bb7 | -3.56812 | -51.44535 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bf714a44-83a4-3fac-9f1d-0987c2535c73 | -2.73854 | -54.13574 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d34c5da-87a1-39c6-a67a-ff02cecaaa8d | -4.1855 | -48.56266 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b026125-152d-3e59-bd90-e3729516c39e | -1.20549 | -51.7769 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a8571f4-537a-38b8-8f98-4ef81748d65f | -1.21344 | -52.48119 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 471f3039-d964-3f7a-bdf7-147b0395832b | -0.94096 | -51.72401 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4c937ab-0f32-3ef0-94e0-85707e8a3166 | -3.98775 | -49.9228 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4da46a32-4294-3cd5-997d-c2189947474f | -3.33365 | -54.06614 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c4e0879-b6c6-3fb9-bed2-b4b6f5e39eb6 | -1.27123 | -52.12871 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README45.md)
