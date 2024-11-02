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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2287d59f-13dc-310e-82ee-a967b2e866df | -2.25407 | -46.66843 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de54cefd-aecf-30a7-9d46-1aa3c40c0bd4 | -2.22976 | -46.69382 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50fad2c3-8d15-388b-bea0-005e1bb2dbcf | -2.22435 | -46.69586 | 2024-11-02 05:04:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906a2ac5-b68b-3262-8706-35283d28a299 | -2.07974 | -47.13451 | 2024-11-02 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 912feb64-21ff-3fd8-894c-e96fb76837ad | -3.43787 | -46.20746 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f97519c-4d26-3720-8aa3-037111208c1b | -3.39935 | -46.06765 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d096745-f4d3-39e0-826a-ba7699f91aaa | -2.46497 | -46.13971 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae1bdd2d-0683-3d28-b9e8-369177b3a8d7 | -2.34096 | -46.14453 | 2024-11-02 05:04:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2339fa32-2e4f-330e-9e16-eacf6695595c | -4.9574 | -46.50266 | 2024-11-02 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8969f803-3160-3699-af4a-21e5586f22ea | -4.95695 | -46.50575 | 2024-11-02 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60cc105c-e6a5-3c56-ab60-80378137e7a1 | -4.7942 | -47.1314 | 2024-11-02 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f4203bc-51fd-3059-9053-32f0ca0d3c2e | -4.77695 | -46.40953 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ac79861-5855-3f03-b2f0-b50d68e8d66a | -4.7765 | -46.41277 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e2771bf-5f8e-34c7-9c6d-1342a362455e | -4.70391 | -46.4355 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6a82904-924b-387f-8ea2-46f690fb80a8 | -4.69865 | -46.43462 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2316bc03-ee4c-3ad1-8ad9-13e20c11bd3b | -4.6982 | -46.43777 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dccd7e1d-02fe-3b04-95e6-a9b634210f62 | -4.67933 | -46.38488 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a612305d-dc72-3bfd-924c-2a2d3a7e0dcf | -4.67905 | -46.38222 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b4dfa453-3a9d-36d9-bc73-1c2362a00fdf | -4.67884 | -46.38816 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 044f3972-b628-3f00-b9d2-3903763fc779 | -4.67859 | -46.38554 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3438c150-937c-365e-9600-01246cd0c7d3 | -4.67813 | -46.3888 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ac4ba57-e9a1-3270-9ba1-dc8c0ca3c3c8 | -4.67457 | -46.38048 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1c94ce5-6b14-3c8e-b599-a8db69cfde9a | -4.67408 | -46.38382 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5142c182-5ff6-3d89-9bce-8b8a729d35a5 | -4.67334 | -46.38447 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f55b77e-cb05-3168-b5bb-c06e7a537a42 | -4.66156 | -46.32127 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ace2493e-8f98-3f5a-92e7-fa1705f0cf32 | -4.65828 | -46.38108 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a719212-df49-31e7-a272-7c63e1e74471 | -4.65672 | -46.31728 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc9529fb-b524-3d01-a183-30b0c27f30a8 | -4.65626 | -46.32045 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 951d29c2-a165-3263-a03e-2e67828035ed | -4.65369 | -46.60205 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3fef79fe-259a-360b-b0b0-16a63f86007d | -4.52456 | -46.4888 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51531534-f71b-323b-b219-d438198617e2 | -4.51931 | -46.48812 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 744eb6b1-4fa5-3cf3-bc9e-32640b925614 | -4.51886 | -46.49122 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aac0cfc4-17a8-31c7-9f18-29e897a4f48c | -4.50963 | -46.62784 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af6c874c-cab5-3fba-b9f4-ecef28d77319 | -4.50448 | -46.62682 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5368707b-f225-3c51-8d86-3f2c07aba3df | -4.37809 | -46.53672 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd5edf89-8343-3bcf-9a88-ee1452358a32 | -4.37287 | -46.536 | 2024-11-02 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6517b5aa-3b58-3826-a58e-274b1777fc5c | -4.30469 | -46.90277 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5148cc0f-6f82-3968-bae2-ce7e99cb9ad8 | -4.30426 | -46.90578 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 984397d3-e040-3b59-8037-3742c026a11e | -4.30383 | -46.90879 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97631759-92bf-3b56-9a99-e2f58e26d02f | -4.25999 | -46.38789 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 074702d6-c20b-3334-8b2b-4e5d6f095d51 | -4.25953 | -46.39116 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6fa3bab-d9b3-3aa0-88b0-32763bcd162d | -4.25619 | -46.85443 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 417795b7-b93f-30ff-9c92-e078ba2dd2a4 | -4.25577 | -46.85732 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a638213e-04eb-30ff-8ceb-91399f108059 | -4.25522 | -46.38366 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 566a6050-9164-3264-99c1-1a3003e41694 | -4.25475 | -46.38701 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eee55e4-f085-3788-a166-fd7d2721739d | -4.25429 | -46.39027 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f787a83-5138-3e3c-ad7a-7e71e29d9d03 | -4.25001 | -46.38256 | 2024-11-02 05:04:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c9c8203-7690-373e-a458-a3f900490f4a | -4.20386 | -46.71003 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44943482-bd02-3be3-a600-82a17081fee0 | -4.20088 | -46.69389 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50c789d5-f8b8-3321-b7cc-682e2cc3ad68 | -4.19912 | -46.70642 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a5ce758-938e-39bf-8a09-374c21037f5c | -4.19835 | -46.69414 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47f4110a-8323-376d-bea9-4e2f1c820577 | -4.19695 | -46.70354 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68d654b2-c580-3edc-9f5e-2acfe323d148 | -4.19648 | -46.70668 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4507453-0ef8-3e03-aeab-5fbeedff465a | -4.19439 | -46.70275 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6adb7b7-c6e1-3407-b212-973d60823fbc | -4.16787 | -46.57845 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d28a5f00-01f3-3365-bf19-ef2163cafb7a | -4.16741 | -46.58167 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e808d05b-20ef-317a-833f-5716b73d14bc | -4.15046 | -46.84148 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2900bdc2-fdd7-3c2d-a717-2ad784fa361d | -4.15005 | -46.84424 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d255e053-aec8-389a-8dad-042e729035d5 | -4.11042 | -46.59859 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1c0a2d0-bd86-3be1-aa70-aae7ee83acbf | -4.10976 | -47.11821 | 2024-11-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adba6416-7438-3ff5-92c8-0bf79bb55fbf | -4.10935 | -47.12098 | 2024-11-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b669775-775b-3399-9b21-137860ea8426 | -4.05358 | -46.9394 | 2024-11-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 264ecd3f-5efa-3fa6-8445-193b2f40eef1 | -3.99191 | -46.4575 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 22afe33a-bef4-3c90-bf69-f1820e5fbb58 | -3.99145 | -46.46067 | 2024-11-02 05:04:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 016030e9-96f5-3a63-86cd-69f0a1e4c168 | -3.89007 | -47.07935 | 2024-11-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abceffc1-2425-364d-b19a-e40693418d90 | -3.88966 | -47.08215 | 2024-11-02 05:04:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db70f934-6582-3a53-adf0-7c4a707c73df | -3.81684 | -47.47549 | 2024-11-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85cd85ef-7f5a-337f-bfc0-8dcde3f59d0f | -3.81199 | -47.47483 | 2024-11-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22105417-f36d-3646-bf79-d9956e204e82 | -3.63577 | -47.30901 | 2024-11-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af9cba26-4465-30c0-8668-978988baa089 | -3.62598 | -47.30764 | 2024-11-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0ce2b07c-51bd-3421-a5c6-2df0fc1cb2e5 | -3.59585 | -47.30888 | 2024-11-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73a8e2c7-3529-3dcf-b528-77305682323a | -3.59095 | -47.3083 | 2024-11-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6328ceb-d893-328e-b3f2-bb92b4e72797 | -3.56163 | -47.38465 | 2024-11-02 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa3c6704-17d7-3522-814b-63b308d2cabd | -5.73791 | -47.1819 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e9f53936-26a0-33ad-aa5b-7dc4bdd98541 | -5.73499 | -47.17842 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ec11b13d-7cf6-39a5-aa48-a484f3494ab0 | -5.73455 | -47.18145 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a07fd320-e25c-37d6-a5fc-5fd1ebec097a | -5.73323 | -47.17815 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2dc9bc3d-e602-36f8-8221-b16836ced662 | -5.73281 | -47.1812 | 2024-11-02 05:04:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 21f4643b-81fb-3739-aed1-92a732a5ac00 | -5.51073 | -47.17114 | 2024-11-02 05:04:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b449dd0-3392-38f0-b9a6-1e9e20304b7c | -5.51031 | -47.17408 | 2024-11-02 05:04:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 542fe169-f734-38e7-89e2-a718d6f0f0fd | -5.50565 | -47.17046 | 2024-11-02 05:04:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57afefd2-24dc-30e9-aa1f-e03349ccc464 | -5.35621 | -47.35413 | 2024-11-02 05:04:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b25133e1-f9c1-3f34-a795-fc8306563738 | -5.35121 | -47.35342 | 2024-11-02 05:04:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4edd8b3-57b6-312c-940c-2a1fe8591abd | -5.29222 | -47.37407 | 2024-11-02 05:04:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7e05ecab-7db6-36ec-b912-621a5bd4015d | -5.29183 | -47.37689 | 2024-11-02 05:04:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a62b444b-7b82-3cb9-b982-7bf3c36560ec | -5.21492 | -47.44889 | 2024-11-02 05:04:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b70dfeff-b7fc-36b1-9366-17d745df43ee | -5.14736 | -47.71367 | 2024-11-02 05:04:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7abf4eb4-c392-34ab-af00-b03eca20c695 | -5.14661 | -47.71902 | 2024-11-02 05:04:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4a7336bb-d471-364f-bf6b-d37beb90b6e9 | -5.06246 | -47.7279 | 2024-11-02 05:04:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30ae9829-7f04-33ed-bb9a-ee53b6487a33 | -5.43388 | -46.50536 | 2024-11-02 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13cf05d4-1b59-3c92-9283-bff5ffd7e70b | -5.21901 | -46.737 | 2024-11-02 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f31b3c13-bcbc-3a85-8822-18ab50ebfdbe | -5.21857 | -46.7401 | 2024-11-02 05:04:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a40e087b-ea01-3642-8a65-15a18d9752bb | -2.11807 | -48.28753 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6a013628-0142-308c-80ef-32ed99290d64 | -2.11361 | -48.28685 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab792c76-1db7-3dfa-a4fa-b6b11568d247 | -2.05361 | -48.56005 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0c6a3d98-e72a-34ec-ac86-ffe16039a801 | -2.02724 | -48.40738 | 2024-11-02 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a726a00-8345-3313-aca4-98158622ff95 | -2.0106 | -47.95015 | 2024-11-02 05:04:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bcebe08-2484-36a6-96f6-938fb441a0cd | -1.82154 | -48.01614 | 2024-11-02 05:04:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d09d392-48ef-3ee8-ad5d-8d5f6efe7a6d | -1.76965 | -47.96107 | 2024-11-02 05:04:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee796625-48c0-3a64-8e87-9fae28f672ad | -1.57648 | -48.70486 | 2024-11-02 05:04:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README59.md)
