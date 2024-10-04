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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d670f76-ad04-3d88-8577-fdf9986feef7 | -12.7899 | -47.451401 | 2024-10-04 00:42:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc3bf9fb-2b4c-3367-b60c-d540dbf7ac3b | -12.7915 | -47.458698 | 2024-10-04 00:42:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35cb16e4-8878-310d-9a26-4c0a874ad488 | -12.7931 | -47.4659 | 2024-10-04 00:42:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc44f900-0293-3ea3-ab9f-41b4131eca73 | -13.5558 | -51.240299 | 2024-10-04 00:42:48 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed59ceb0-6b65-32b3-a566-405ff8308cf1 | -13.5581 | -51.251301 | 2024-10-04 00:42:48 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30063966-fc5f-3766-b1ce-c4c2d644dce6 | -12.2605 | -45.963799 | 2024-10-04 00:42:51 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 755e71f3-c891-3478-802c-0251080facfc | -12.3779 | -47.681198 | 2024-10-04 00:42:55 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1e4abda-a54e-3305-9d2d-0da718e77b98 | -13.0976 | -51.144001 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cfae6c39-3ac5-3f29-9e3b-12a0d3d33fd8 | -13.0998 | -51.154598 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b103aac-2525-3252-be02-111b4a4b5ce8 | -13.102 | -51.165401 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04f8f3ac-a0f5-3acc-ba0c-28cbdfb07c42 | -13.1042 | -51.176102 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b77122b7-2fe4-3872-a015-4f4321a45292 | -13.0901 | -51.1567 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1db6516-895a-3fa2-9302-38a5c28f0324 | -13.0923 | -51.1675 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fbd83fb-3d2b-3af9-84f2-126a03ce9737 | -13.0616 | -51.118198 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac582618-f040-3388-ab21-99b32eff4267 | -13.0638 | -51.128799 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 869bcf5a-a2f7-317f-9c54-9cba975e1391 | -13.066 | -51.1395 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| acb0f234-0da0-394d-8528-2d471c8fe446 | -13.0683 | -51.1502 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b8ab033-4db0-3132-8bac-ef8daff28db0 | -13.0496 | -51.109501 | 2024-10-04 00:42:56 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 62e0d5e6-3c32-3bcd-a313-56d1dac9ee5f | -13.0518 | -51.120201 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3cfc128a-7293-3d26-b82a-24a5ff8f2914 | -13.054 | -51.130798 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9d024a06-c1a2-342a-82de-733ab548941d | -13.0879 | -51.146099 | 2024-10-04 00:42:56 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58b322ee-9e97-38f5-a72a-7bd03088759e | -13.0323 | -51.124298 | 2024-10-04 00:42:57 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbe243fa-5310-3c3c-8b4a-a3a560db5df0 | -13.0225 | -51.1264 | 2024-10-04 00:42:57 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 119b889f-863d-3d28-b644-8fb1f91ef76d | -12.9986 | -51.1092 | 2024-10-04 00:42:57 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc0b62b-e7f5-34be-8e82-da1b52398cb7 | -13.0007 | -51.1199 | 2024-10-04 00:42:57 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 840dfd50-d9f2-3e1e-95f8-23191c0c446b | -12.979 | -51.1133 | 2024-10-04 00:42:57 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eebe0140-ad56-3b37-987a-611abb95eb0c | -12.9812 | -51.124001 | 2024-10-04 00:42:57 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3960b262-8fe7-386f-9f0e-a40e80c08934 | -11.278 | -43.385502 | 2024-10-04 00:42:57 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4aade060-cfd2-31fd-8926-02272038e210 | -11.28 | -43.393799 | 2024-10-04 00:42:57 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0dac75cf-4ee6-30e6-9442-afa887f56b2a | -12.9693 | -51.115398 | 2024-10-04 00:42:58 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c4c691c-59ad-36a8-9082-f5dda079e360 | -12.9714 | -51.126099 | 2024-10-04 00:42:58 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45550b6b-9afd-3f9c-84e7-b2afe71e9dd4 | -12.9736 | -51.1367 | 2024-10-04 00:42:58 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0350cc8b-be1e-34fe-9b11-41e303bc195f | -12.6096 | -49.646801 | 2024-10-04 00:42:58 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0055c9e-2d66-3092-bab4-0c3b7d13b204 | -11.1097 | -43.329201 | 2024-10-04 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b05222ea-db42-3019-bdae-c8c7c2c1f0f3 | -11.1117 | -43.337601 | 2024-10-04 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6d862d21-2dfe-3e68-a2db-c1cdb7cf916c | -11.9766 | -47.3564 | 2024-10-04 00:43:01 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02aec305-69c6-3e12-b481-55a70a2332d8 | -11.9782 | -47.363499 | 2024-10-04 00:43:01 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 625a9d49-e133-34ed-baf5-41794872bf32 | -11.9438 | -47.3937 | 2024-10-04 00:43:01 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e31db4d-35fa-3101-8e5a-68642856ba36 | -11.9454 | -47.400902 | 2024-10-04 00:43:01 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f53f5bbe-6c53-3458-9a10-eb14e8ca4d28 | -11.7863 | -47.5644 | 2024-10-04 00:43:04 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9998a641-3c51-3025-9100-09f8f28212c0 | -11.7879 | -47.571499 | 2024-10-04 00:43:04 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20da657a-96cc-3685-8b20-4784a68f391c | -11.9007 | -48.314701 | 2024-10-04 00:43:05 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6db706dc-e1dd-330c-b17b-bf4f968f015b | -11.7123 | -47.694199 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef97265a-b64c-3a35-b37f-85baf6f9eeda | -11.7139 | -47.701401 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 502fe670-7e37-3523-b106-35c1b9ef4bb0 | -11.7009 | -47.689201 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e47318e-f4a0-314b-84a7-ce59e43f7ef5 | -11.7025 | -47.6964 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4649933e-a13d-315d-bd57-c653991b5c66 | -11.7041 | -47.703602 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a00358b2-18de-316e-8fce-2e92101d45cf | -11.6895 | -47.6842 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1d4249-c4ea-3740-b2e0-cd152273bee0 | -11.6911 | -47.691399 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8597baf4-dc9e-3d31-a591-ccb54f2a698d | -11.6927 | -47.698601 | 2024-10-04 00:43:06 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c0c3a31-4d55-3ef6-abb1-4aa956f2c205 | -11.6797 | -47.686401 | 2024-10-04 00:43:07 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2dec99e-9bf3-334c-9383-b22315af826a | -11.6699 | -47.688599 | 2024-10-04 00:43:07 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d03b2932-c73e-341f-87f2-bc7c1a4c9594 | -11.6715 | -47.695801 | 2024-10-04 00:43:07 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37e6ca9f-d5de-323d-8040-50adcb1a5bb7 | -11.6601 | -47.6908 | 2024-10-04 00:43:07 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5038e059-a457-313a-95c8-ab4ec25ca647 | -11.6617 | -47.698002 | 2024-10-04 00:43:07 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d674a689-e3c3-39e0-b446-0e44c7fd470d | -11.6633 | -47.7052 | 2024-10-04 00:43:07 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d21a3858-5205-3a5a-90d6-0fa375b9718a | -11.6503 | -47.692902 | 2024-10-04 00:43:07 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec083dd0-ac45-3967-be74-5db700961e97 | -12.1486 | -50.464802 | 2024-10-04 00:43:09 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db34318e-b4d5-343c-8c96-613f34c6b240 | -11.3875 | -47.2075 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa91b014-45ba-35f6-8d34-b10be3e871ac | -11.3891 | -47.2145 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1083191-5ec1-3bbd-9b0e-87bef7b5a353 | -11.3907 | -47.2216 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97baa14d-eb1c-3232-a2fc-de46d4021beb | -11.3923 | -47.2286 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad11390-4a19-39a6-8c2e-e15277e8cb30 | -11.3777 | -47.209702 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4453ab2-fc62-324b-8f19-7ff8be292963 | -11.3793 | -47.216702 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abeb5077-4add-3b57-8296-182f57cd979e | -11.3809 | -47.223801 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b5f44a5-0ee5-31a1-a375-9030afb4ecd3 | -11.3825 | -47.230801 | 2024-10-04 00:43:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80ed5882-1171-3064-bca7-7fdc65d690ce | -12.5939 | -53.1175 | 2024-10-04 00:43:10 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dda4972d-5744-3a42-8dee-1ed34615679f | -10.7427 | -44.618198 | 2024-10-04 00:43:10 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 494656fb-51b2-37da-92c2-3cd3aac37cce | -10.7444 | -44.625702 | 2024-10-04 00:43:10 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| acca80dd-57ee-37fc-9292-88cad8ae6309 | -10.7462 | -44.633202 | 2024-10-04 00:43:10 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec5e9ea7-bb6f-3f0d-8529-02fbc0a560a9 | -12.5813 | -53.1054 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e651457-3644-3434-ac76-b30868e8f5fc | -12.5841 | -53.119499 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a90c144b-817e-3ecf-ad24-95e914094b20 | -12.587 | -53.133598 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9d2baf6-9553-36e8-9a87-fb0aa4ff35f2 | -12.5715 | -53.107399 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4b37161-277b-3b52-8ab8-4886f63d9cc4 | -12.5743 | -53.121399 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed92e1c4-d244-3963-8c15-cf05859415b9 | -12.5772 | -53.135502 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb065400-29cc-3f28-8deb-ae962b3de18d | -12.5618 | -53.109402 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3626a2c9-bb56-321f-947e-ab331f615d95 | -12.5646 | -53.123402 | 2024-10-04 00:43:11 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ade0096e-766a-3b87-8180-7a43da3cce14 | -11.2282 | -46.9566 | 2024-10-04 00:43:11 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbe4bdf7-831a-3551-a2ef-cdea381a573d | -10.5133 | -43.8629 | 2024-10-04 00:43:11 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40c0c629-8d26-30df-918e-324641b778f5 | -10.7346 | -44.627998 | 2024-10-04 00:43:11 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c124ce3c-3eea-377e-a8b8-d0ea8cd12993 | -10.7364 | -44.635502 | 2024-10-04 00:43:11 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12c9b8d2-5eed-337c-b5e1-f8d539f60869 | -11.0917 | -46.490101 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2608b2b-c3a6-3662-ad4f-7added30b46c | -11.0932 | -46.497101 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d8cca0f-cf73-3d19-b0ea-007b60d78002 | -11.1893 | -46.921398 | 2024-10-04 00:43:12 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34b3e68e-3a00-36b0-a0ee-029d4d7c4c85 | -11.082 | -46.492298 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3843aabb-2fa8-3ca5-ab72-f78a7781a640 | -11.0835 | -46.499298 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94bdc7ed-7d8f-3e6a-b14f-3d995ab3e037 | -11.0851 | -46.506199 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bafeeb79-616e-3c27-bbf2-7cfb3f78bf3a | -11.0867 | -46.513199 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15465635-83fa-3884-ba40-cb61650250ba | -11.0883 | -46.5201 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b66f0ff-cab7-3510-9650-4e20e153da94 | -11.189 | -46.9655 | 2024-10-04 00:43:12 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71b507b4-06e5-36dc-8124-36204771ac0b | -11.1905 | -46.972401 | 2024-10-04 00:43:12 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0088f52e-3bc1-31d9-b3ed-a5964c9c34c2 | -11.0769 | -46.515499 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f381ec45-053e-3fca-9103-476bc624a19f | -11.0785 | -46.5224 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 132b9c85-82fe-3bc2-8c57-80e8bb2c4b40 | -11.0655 | -46.5107 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a7d6685f-e303-3b9a-81e3-36b938f38e83 | -11.0671 | -46.5177 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 532630b9-e419-3bbb-a71f-347ff7873407 | -11.0557 | -46.513 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 85fe1f2f-c2c8-3c05-ba1d-588c5bd6b149 | -11.0573 | -46.52 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 406a1b43-e859-3b10-8f66-8edc4423b7df | -11.0589 | -46.526901 | 2024-10-04 00:43:12 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b334863e-e028-32fc-ad73-94b8c52024e3 | -11.0443 | -46.508301 | 2024-10-04 00:43:13 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
