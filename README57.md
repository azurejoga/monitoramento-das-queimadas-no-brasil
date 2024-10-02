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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fc0914e-45b1-308e-a9cb-5eb8f11ca651 | -22.38669 | -49.29913 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 86e8f9a1-0cd2-3682-8457-fa097a616bd5 | -22.3865 | -43.52508 | 2024-10-02 03:34:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 632bd4dc-446c-3dfe-b062-79598ebff121 | -22.38528 | -49.30492 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| 90900ba5-ff04-3d6c-a659-2cb99400621a | -22.38524 | -49.29611 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 907d2033-4749-3b8f-9000-ef9d6c47a40c | -22.38522 | -43.52316 | 2024-10-02 03:34:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7dae44c8-18e1-3aac-b673-8d72c8ab4c9c | -22.38459 | -49.27921 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| fb4a5435-2ad6-3dfb-b844-eb0c1553f06c | -22.38402 | -43.52909 | 2024-10-02 03:34:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ceae30c6-b893-330b-8ff6-dc8650238d2e | -22.38388 | -49.31068 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.3 |
| a8fb0819-a267-3ae4-b8be-7b7c19e932bd | -22.38379 | -49.30193 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 4838b443-9b4e-3fd5-90ab-b4fd9eef4224 | -22.38304 | -49.28563 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ffe45d32-3ed9-36a0-a5ef-6fe04ed5c528 | -22.3825 | -49.31637 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 54e0722a-306f-37d3-bea6-cdded5469e7b | -22.38234 | -49.30773 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 21062465-a436-3764-bf23-556134116cb3 | -22.38175 | -49.28229 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 60999945-3955-3a4b-b09e-f3e45b00e031 | -22.38167 | -43.5248 | 2024-10-02 03:34:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4f412a85-8086-3019-b31b-332919201f93 | -22.38155 | -49.29173 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 721c331d-bf91-3bde-ac2c-d9666c6f90e0 | -22.38091 | -49.31348 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 527f6421-a0e8-38fd-8813-b24d4862de26 | -22.38014 | -49.28875 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| a12b22bb-d18c-3dba-ab43-bd78117ccdb2 | -22.38013 | -49.29755 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| fed7a34c-56e8-35e6-beb1-3d3a3ebed308 | -22.3795 | -49.31911 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 3d904a90-4557-3455-8fc2-94d5dce0a9ab | -22.37921 | -45.79119 | 2024-10-02 03:34:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 376a79dc-2042-35ba-89fb-711d4e8763c4 | -22.37869 | -49.30346 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| bdd38fe5-873d-3c00-b412-91b081be11b0 | -22.37869 | -49.29455 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 58ac3f6c-5115-3ba5-8269-4e8d9702f347 | -22.37727 | -49.3093 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 013add6b-9104-39c5-8dbe-5024338ec170 | -22.37721 | -49.30043 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 3f65f38f-9f1a-3839-bb79-545221e6928f | -22.37652 | -49.28391 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4a86dd48-9c39-3932-b458-df10e1d62771 | -22.37589 | -49.31498 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d26e3e9d-4ccd-321f-a92e-9749ef4d9683 | -22.37574 | -49.30631 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| b69f9d83-3f4f-3f10-ab7d-10e8726a71dd | -22.37524 | -49.28057 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| a0ff8e10-ca69-34b2-a9a5-7fd9ac4e0c34 | -22.37499 | -49.29017 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| 885735ea-d60a-3015-b75b-409670699a05 | -22.37429 | -49.3121 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 48a439fe-6367-3692-912a-7e517db567fa | -22.3736 | -49.28711 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| ca9998fa-c101-3ee0-82a7-d4c70c70195a | -22.37357 | -49.29603 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| c739c709-b0ba-361e-b21d-a3209e02788b | -22.37212 | -49.30195 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| fe9a2920-85c1-3373-8b27-703864a909aa | -22.37212 | -49.29304 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| d534f6f0-9030-39ac-9f5a-425e761f7a8a | -22.3707 | -49.30777 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 6cd9a916-a78f-383c-a9e6-6a45067880df | -22.37065 | -49.29887 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 264ab2c5-3294-3d3d-9e30-59ce3e1517c0 | -22.37 | -49.2822 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| dd9d22a4-341e-3a7f-9d04-3e0de2278158 | -22.36932 | -49.31344 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2861a89a-4d50-3062-ad52-c2ad6f92c692 | -22.3692 | -49.30468 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 80ee601d-baa0-3c49-9820-39b8a546aad9 | -22.36867 | -49.27907 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2b0d72c3-d4f9-3e14-9b52-33c5b826c1ab | -22.36847 | -49.28846 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| d659a54e-cd34-3d04-8462-018006e64e5f | -22.36777 | -49.31037 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| e6125a8a-f2d8-34d8-b929-f0f104c9df2f | -22.36709 | -49.28537 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 260ca79f-d64e-33c2-b4e8-a308b0c5aaed | -22.36708 | -49.29415 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 1f6065eb-4c20-3230-8c4a-fe6995d19f44 | -22.36568 | -49.29987 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 989876ca-b238-3db1-8632-82d847dc5d6c | -22.36563 | -49.29118 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 49117858-cefc-39f1-b3e8-fa7f8c235a51 | -22.36427 | -49.30567 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 5907e3f7-2748-37b9-93be-49c1d723c36c | -22.36424 | -49.29673 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 25c0ff86-4095-343b-9e66-aa48d21b6759 | -22.36343 | -49.28069 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| be999fe0-c63b-38ec-8a44-348fb840b5b2 | -22.36286 | -49.31142 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 5f5bcb99-5511-3f8a-8e96-63e28f559217 | -22.36278 | -49.30252 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| e369359f-7867-31d4-8554-ee156157d639 | -22.36202 | -49.33328 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a579c77c-0c0e-30cb-9589-d53a0fd7ccdc | -22.36197 | -49.28666 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| ff0b0efb-d072-3d2f-b6f8-9410c22043ef | -22.36133 | -49.30832 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 23d33fa8-3c27-3e4d-9f3b-c1fb77eeb9e6 | -22.36062 | -49.29216 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 7e496e0a-93b6-3696-b7ee-35c250086708 | -22.36059 | -49.28357 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| bcf88ce7-c881-3c44-99d6-e3fc7319cd4f | -22.35984 | -49.31424 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 26635fb5-b49e-36dd-b495-63c6163f8749 | -22.35926 | -49.29772 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| cb5b3abe-7e8e-3812-8f21-fcf191bdf9e0 | -22.35916 | -49.28927 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| dc6ed72d-45e3-36cd-87d7-01bd82bdc401 | -22.35855 | -49.32906 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0f21ddcd-bf6b-3a25-b809-c85e1be37321 | -22.35793 | -44.01771 | 2024-10-02 03:34:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 218f556b-0d60-3c5e-a1f8-2d8e57cbe7a6 | -22.35783 | -49.30359 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 4ffe8f98-ba72-3cae-a313-8db472c197e9 | -22.35779 | -49.2947 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 6fc09053-979f-3631-8b8f-522f32e16318 | -22.35715 | -49.33481 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 8b90d693-b44e-3cd0-a230-c877395b8e4b | -22.35683 | -49.3262 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| d52a3b7b-628f-3142-901b-780af72ae55f | -22.35678 | -44.02321 | 2024-10-02 03:34:00 | NPP-375D | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 94db6906-6d95-3302-84df-f6999054ebdf | -22.35636 | -49.30959 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 18e04e8b-1c3f-3691-957e-d9e4d4a1f24b | -22.35634 | -49.30046 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| b50a75fb-7aa9-32d8-a2f1-e8f068f6d032 | -22.35583 | -44.2292 | 2024-10-02 03:34:00 | NPP-375D | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 85fdf474-08be-37d8-9d27-0d65d28b4899 | -22.35571 | -49.34068 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d3555485-8e67-3916-8efb-2ac6a7904db1 | -22.3554 | -49.33191 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 37e8fb55-4153-3bfc-b861-47f0e0d03613 | -22.35485 | -49.3064 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 1c7bbb9d-0fea-36da-b6b3-a00b1423df17 | -22.35484 | -49.31582 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 390bb3fd-db65-369d-bb49-6d27d4bd38e2 | -22.35397 | -49.33762 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 20a43a81-8b47-38db-a113-b138407c908d | -22.3528 | -49.29574 | 2024-10-02 03:34:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b3d8619b-866f-3013-a2aa-0ee00005c6f7 | -22.35191 | -49.32778 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4b179778-974c-3263-b4eb-a864ca7df52e | -22.35132 | -49.30179 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0e034a61-4dde-3cc3-b00d-6a88e3800654 | -22.35098 | -44.22798 | 2024-10-02 03:34:00 | NPP-375D | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8356cf89-c474-37e3-b11a-24e6cbd7b15c | -22.35048 | -49.33361 | 2024-10-02 03:34:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f6a8e5dd-15cf-36db-b0ce-658104971d16 | -22.34996 | -44.22718 | 2024-10-02 03:34:00 | NPP-375D | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 53b97881-6d7a-366e-91e0-8e7c1fe80e98 | -22.34974 | -44.23376 | 2024-10-02 03:34:00 | NPP-375D | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d2cb999f-6131-359a-874e-68a66818cb8b | -22.34876 | -44.23299 | 2024-10-02 03:34:00 | NPP-375D | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 51a09b33-aa16-34de-9662-a45f7567787f | -22.34671 | -43.35533 | 2024-10-02 03:34:00 | NPP-375D | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a6cd6d56-ea6c-3822-997e-bbcefc9238bd | -22.34562 | -43.36061 | 2024-10-02 03:34:00 | NPP-375D | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 76efbc7f-e3b1-3470-ad4d-69fe1b9f14b3 | -22.31153 | -45.79075 | 2024-10-02 03:34:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e4bd4421-9e2f-395e-ab41-3575996d187b | -22.31067 | -45.79452 | 2024-10-02 03:34:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e3bacfdb-9863-3382-a54c-46b829a616fd | -22.30999 | -45.79053 | 2024-10-02 03:34:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a2c1f3ce-17b5-3f15-bdca-632060dc804f | -22.30915 | -45.79433 | 2024-10-02 03:34:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 76e70373-b03c-3489-aba0-b903a4a3d6f7 | -22.30411 | -41.88364 | 2024-10-02 03:34:00 | NPP-375D | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2c296719-4c42-3134-bdeb-65edead626fe | -22.21683 | -43.16157 | 2024-10-02 03:34:00 | NPP-375D | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b62bfde7-955c-3f1e-93d6-45f57d76847b | -22.11453 | -45.09055 | 2024-10-02 03:34:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fd98bfb6-21f4-322b-9b57-ce97dbd5f1cb | -22.11381 | -45.09386 | 2024-10-02 03:34:00 | NPP-375D | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 911c584d-c691-35cb-80c3-651adf9eb0d4 | -22.03132 | -42.48161 | 2024-10-02 03:34:00 | NPP-375D | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 91eb23d1-411c-333e-a7f9-27813375d181 | -22.02784 | -42.47601 | 2024-10-02 03:34:00 | NPP-375D | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e78928bd-22dd-3430-baa1-7b1acc9123e3 | -22.01138 | -44.50811 | 2024-10-02 03:34:00 | NPP-375D | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| abc673f3-e393-37ac-a94f-e77b6577a452 | -21.93346 | -41.55457 | 2024-10-02 03:34:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 35aadefe-b162-3359-bea5-ba6234007b81 | -21.67765 | -43.95592 | 2024-10-02 03:34:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a00cf7e4-617e-3474-9fdd-dc47ca3d6eca | -21.67287 | -43.95446 | 2024-10-02 03:34:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3df1a34a-2f59-3f67-bd22-62f888970f33 | -21.66907 | -43.97252 | 2024-10-02 03:34:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7c0adc4f-9378-3832-86b9-3a2846daaea7 | -21.66801 | -43.95338 | 2024-10-02 03:34:00 | NPP-375D | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README58.md)
