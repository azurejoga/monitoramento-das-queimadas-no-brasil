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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84e9716e-ceda-36fc-a18d-681bad8308f0 | -13.44061 | -45.88733 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bafb681c-3912-3f67-9375-748bc0d9ed47 | -13.62862 | -46.91753 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65878c91-3533-3d16-8d2c-723833273204 | -13.57892 | -46.99028 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04e166c2-828c-3a7f-aa34-e5fe355e0a7d | -12.92815 | -46.12353 | 2025-08-17 05:06:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47a69f88-5274-3028-9c7b-3989d7cf78e7 | -11.36439 | -55.41629 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dceeea9-5b44-3b91-bac3-888ac63a5597 | -13.43183 | -45.89661 | 2025-08-17 05:06:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67523197-4be1-3c48-bd49-da13df68ca4f | -13.87761 | -45.54604 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f36c587-0e6e-3118-bcf6-08a23c8d8926 | -12.19602 | -47.24271 | 2025-08-17 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e625f75c-8f80-34af-b82c-892f08a79cff | -10.83354 | -45.32538 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17f52269-020a-36d4-b512-bef69df57303 | -10.85521 | -45.3434 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b55dcb03-f025-3418-ba89-7e6b3dacaadf | -12.89098 | -46.11551 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33784b21-7438-34d6-be40-aea78c0d8a41 | -14.58977 | -47.94665 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0491fbcd-1471-3c70-b962-d3ce6e4b0e99 | -10.83426 | -45.3607 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ea5c180-9f1e-342f-b9d6-0296f3cd479e | -12.85537 | -46.0484 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b2a3ccf-a5f0-3803-851e-1420c2db04be | -8.98626 | -60.53008 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d7126cb-9db6-3415-b8d1-fff6f3590264 | -8.99983 | -60.51809 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8973d08-0c60-3468-aa06-1b7ef49853bf | -8.81896 | -52.04679 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9bf12065-1f84-31b8-b7e8-fc04ca284fd7 | -10.87854 | -48.5 | 2025-08-17 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45bd5e6b-db81-3703-8f04-cfa938fb65c2 | -8.99831 | -60.5038 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52d2c621-ec2d-31ca-83f1-b0e4b5a61e9e | -13.43212 | -57.03304 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11532e5c-09f8-3f3b-94e8-d39003c7e187 | -12.87156 | -46.06941 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2b2ad91-4bc2-33eb-9ebd-1ac06bfd6474 | -14.59946 | -47.95915 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37b3e8c4-57cd-3613-abd7-92a7b421ad01 | -11.36952 | -55.42843 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cf30efc-3aa1-3e16-aa4b-d32fad62fe2d | -8.86912 | -68.50584 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04ebad18-f8f4-3835-ba58-1a7c8f35ef6f | -12.19138 | -47.23387 | 2025-08-17 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 670e45b5-37b5-32a7-a0a4-16f896480ccd | -10.30823 | -52.55787 | 2025-08-17 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41349911-0a5d-3436-9ee5-2db17ce4eaa0 | -10.11755 | -57.75974 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 534b5f81-80f4-3fc8-b69e-b5a1deb9199e | -9.18417 | -59.69302 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9f131fe-07c4-3c3c-82b2-4fccbc9a395d | -8.99606 | -60.51748 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f3b68d9-4d0a-3ca2-a5b1-410eab699867 | -13.5904 | -47.77065 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a28d940f-3369-3302-9afb-7de848c24bee | -13.01128 | -56.85289 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ca570b2-76da-3965-84c0-f630ebe03acf | -8.98403 | -60.49673 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ac722b35-88fb-3508-9bfb-d4d82070b5bb | -10.83482 | -45.35579 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48bbbf86-3c36-34fb-9fea-223a0f34d29e | -8.99678 | -60.51657 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e04b9256-6270-3a68-ae13-8c024b83a1a2 | -10.82557 | -45.33902 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95ffd40b-e930-3815-8947-32c380adeece | -9.51017 | -60.53473 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea33807a-395f-3591-a1b5-71bbeb869770 | -9.51164 | -60.54902 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 663979b8-8ec6-3890-a3ea-b83ce032cc0a | -8.98703 | -60.50194 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ce0430-8460-3f4f-b18a-809a434c4c3b | -13.60265 | -47.76183 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 606e54a7-a8f3-3ab0-8d4e-b60a4170bf53 | -8.99079 | -60.52607 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a52e7215-ac7f-3474-b3d6-40cb7e7d6a58 | -13.00246 | -56.86603 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e9c25bb-14f3-3218-9de0-05d7abbd35c8 | -9.22391 | -59.6529 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a5d51bc-9143-316a-ad4f-2d532de75cd8 | -8.81829 | -52.05149 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8f50ba1-7427-37e2-a44b-bf6aa489c793 | -10.43686 | -60.28842 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d0a2033-ca29-3c6f-8f15-92a38fb09163 | -14.59427 | -47.95538 | 2025-08-17 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bb106227-930e-3abe-abac-b126d6327323 | -9.5527 | -63.66904 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb4c43c8-f0dd-3827-89db-dd4e7ae40e7f | -8.99911 | -60.50291 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 870a8da8-e23c-33ec-a6da-6b90541d9095 | -14.3629 | -47.04836 | 2025-08-17 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee94186-babd-37e5-8aba-ea11b4ff0e54 | -12.86541 | -46.06908 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd4d4d8-474d-3cca-b07b-98ed35352b80 | -12.57298 | -47.05209 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c22385f4-6eec-3b45-9200-dd480bb02553 | -12.14394 | -47.9149 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 191077ee-c759-3711-ac8b-41b8ae2d3d92 | -12.14081 | -47.91654 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 790e262a-e188-3b35-a61b-5f2e99bc9237 | -14.93299 | -47.05651 | 2025-08-17 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe676de3-8f61-3f4e-b554-4f6977eabc7e | -8.99079 | -60.50256 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f70d008-9b1b-33d2-a641-c5e447bfece6 | -8.7924 | -52.03072 | 2025-08-17 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 35f463a7-a130-38a6-94f1-c43a09dfb4ce | -9.50563 | -60.56206 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc6e56e6-0a48-32f7-9fb8-46a0f4ea2f85 | -12.1909 | -47.23783 | 2025-08-17 05:06:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c9518f8-1216-3b48-a6de-5b25a382d59c | -12.11984 | -47.90961 | 2025-08-17 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91a18099-40af-3682-8876-8614f08e734e | -9.51167 | -60.52566 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5c696e99-14e0-377c-a2c4-284f30d66335 | -13.61461 | -47.75557 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d03a753a-8882-3e6e-bcd9-9b8983dbdaaa | -13.01019 | -56.85999 | 2025-08-17 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 803f4034-a8ab-3a91-91c7-c492fa4ed963 | -9.50188 | -60.56142 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc807e4e-8c47-3d73-b2e4-4225fa5e409a | -9.22169 | -59.644 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a92cdbd-3877-36d0-8f05-72813ef5ef8b | -13.60647 | -47.77713 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f93d415-500a-35ea-9409-ebc55f719e8f | -8.09501 | -54.98922 | 2025-08-17 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f7432dc-3ed7-34d6-86b4-f8917018eca2 | -11.35982 | -55.40043 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5595dcc-2507-3c6f-8d2a-6f69c1b2d52b | -8.88233 | -68.51945 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de60139c-beb5-3af6-8580-3e59f9813094 | -12.86096 | -46.05374 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd36d807-40ce-32bb-aae6-8c93b2ef7f37 | -8.88335 | -68.5142 | 2025-08-17 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a53f138-296c-34a0-8aec-5f2de2ae2bd7 | -10.83979 | -45.32617 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe5282ab-3b35-3345-ab83-7e9cf6eda4a5 | -8.99455 | -60.50319 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40ed8906-eee2-3260-be0f-6dff4a2b320f | -13.61123 | -47.78444 | 2025-08-17 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8270bc2-e357-3738-9205-5c240e5678cc | -9.20033 | -60.82936 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5279f037-ec82-3547-9f7a-1bfbb285f939 | -10.84423 | -45.34179 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| acb968ba-d66c-3fc3-87f8-693d81aebdfb | -9.1673 | -59.63928 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a0478b5-4d33-3ed0-bb5e-2f242f6ba731 | -9.17004 | -59.62284 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e043d341-353f-31e4-b6d3-2a29b56cad2a | -9.61266 | -65.37714 | 2025-08-17 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8a759f3-5737-34c9-bbfd-089b7bfcd8ec | -9.14551 | -58.29799 | 2025-08-17 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7c7c5aa-9bc6-3b1c-b583-9b31f945eb8a | -9.00133 | -60.53251 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12946bed-e5c8-3d3c-a625-5d315523fc73 | -8.98988 | -60.53433 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f5e7488-29ee-3441-aecf-1407fd79a0bc | -9.20716 | -60.83541 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ce81db1-fe17-33d5-b1b6-3b434e08ca41 | -10.84048 | -45.3616 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ed78070-4a0a-3061-92b8-e71971b9f0db | -9.21521 | -59.63868 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1e071ef-1ce5-35ba-9b13-dee89d3c15e4 | -13.61363 | -46.89312 | 2025-08-17 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e611d1d4-cc19-36d3-bba4-d28456d040b6 | -10.83762 | -45.33116 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69f0ffd3-f6df-3fc2-b0fd-ca53293015bb | -11.36328 | -55.4237 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c04ba305-deec-3c3a-83f6-5c1e65471714 | -9.00057 | -60.53714 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 375c3dc2-dc82-3843-acc8-482cb8da2397 | -9.5139 | -60.53537 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb80a74a-9293-30db-ba7b-cda111b1e26a | -8.99304 | -60.53589 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee8254d7-7f03-3a6b-8fd9-c7040d33de64 | -8.99145 | -60.52513 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01ad92b4-75f5-3e47-bdbb-67e9ec796ee2 | -12.62014 | -46.91307 | 2025-08-17 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6201a65c-cc7c-3659-bd63-c11d41a1df93 | -14.18849 | -45.33389 | 2025-08-17 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8827d84b-bd44-3bd3-9755-1a69b5eaaff7 | -12.89041 | -46.12037 | 2025-08-17 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61fef3fb-c106-3a9b-9e1c-b0e6db1d6791 | -11.36093 | -55.39302 | 2025-08-17 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 57b336a3-817d-3e77-a96a-cf14d58f48b9 | -8.98103 | -60.49151 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 76912f93-1bc3-3ac5-8992-b2b08e7a657b | -10.8484 | -45.34766 | 2025-08-17 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7feefc0a-4528-36ca-955b-08c924447784 | -8.99003 | -60.53069 | 2025-08-17 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a837b172-b74a-3fda-a9d4-468f0b111624 | -14.93887 | -47.05727 | 2025-08-17 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d02e19b4-f506-30de-a700-d079d7ec66cc | -9.50866 | -60.54381 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ffab2a1a-aa60-32f4-a7bd-716e146b7874 | -9.92385 | -60.48175 | 2025-08-17 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README31.md)
