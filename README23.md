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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1a7aae8-b612-3522-8fb3-7a8c78862dbb | -16.8659 | -55.834301 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ea20864-f2a3-3128-b5fd-b5f319f52b59 | -16.8675 | -55.8414 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4652074-979e-31fb-98b1-ae743e7eb410 | -16.868999 | -55.848499 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| acb68f4f-4e29-39c8-addc-7fe695dc7fbf | -16.945299 | -56.192001 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec3600d0-e362-3818-8265-f5d7ab3e20ef | -16.9468 | -56.1992 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7bf9527-4f08-3abb-933c-10112f2b6441 | -16.9484 | -56.206402 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc8dc010-4edd-3474-9037-8d012b5d58d8 | -16.950001 | -56.213501 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2469b0e-5895-3e36-807a-c37e5103c2a9 | -16.951599 | -56.220699 | 2024-10-02 01:23:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 80d8d6b7-6862-34c8-b74e-a9fc5e02e21d | -17.0564 | -56.698299 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 354a053a-3ce8-3c33-a603-bd216ac0b7dc | -17.058001 | -56.705601 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 193950a6-cf5d-37aa-a38b-dc4b6c53abed | -17.059601 | -56.712898 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92b10bc4-546d-38ce-9e06-0d8623f8ed7d | -17.0707 | -56.764099 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b66a3a4-41ea-335f-873f-521f0bfceeb3 | -17.0723 | -56.7714 | 2024-10-02 01:23:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8b1ccd00-fbb1-3fc6-a9b1-d0818dd0dd45 | -17.200899 | -57.366699 | 2024-10-02 01:23:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59abe6f9-68cc-3ab7-802e-a3dfc1edd513 | -17.2026 | -57.374298 | 2024-10-02 01:23:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6b8cd7d-2d07-3436-8068-e89ddb242b31 | -17.204201 | -57.381901 | 2024-10-02 01:23:52 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60691ffd-3371-37db-9556-a279edfd9f21 | -16.851299 | -55.815102 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c21ad63-2861-3556-b291-8731b46bcaaa | -16.8529 | -55.8223 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd9ac108-a655-35f5-8d12-6621ccb0c25f | -16.8545 | -55.829399 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e8f39855-2cea-3de3-a807-5eaa41e7559b | -16.8561 | -55.836601 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0bb81664-8fb8-3b05-b828-57df1a009e17 | -16.8577 | -55.8437 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 465e4b29-184a-3942-9ae1-2bceaddfe5ef | -16.859301 | -55.8508 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2bf7397f-a99d-3201-8902-1f2fc02eb064 | -16.870399 | -55.900799 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a10449e-f64d-3fe2-a92b-fd7b0f26d624 | -16.872 | -55.908001 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a44cdb8a-e644-33d0-bc3b-ddfcb4987f2d | -16.8736 | -55.9151 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60a5d8a7-5e20-39a5-8be3-c1608e08eed9 | -16.8752 | -55.922298 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71436454-cffd-328c-9888-f206fd074bd3 | -16.876801 | -55.929401 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11d41f9a-4476-3373-a35c-db9993104399 | -16.878401 | -55.9366 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd9c56ff-c5bc-318f-812a-05d448cb8eb4 | -16.938601 | -56.208698 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 71542ff9-b7c7-3f16-819e-abe2e7d5fee0 | -16.940201 | -56.215801 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ca07277-7604-3d84-9a45-bf840aa1cb0f | -17.048201 | -56.707901 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c89c37f8-67a4-3490-9f61-d10fd379aff0 | -17.049801 | -56.715199 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c2745e4e-4b87-3ff4-9281-9d8601e55040 | -17.051399 | -56.7225 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c5c7185-b53a-3547-a6ce-2bb10ba0e5a4 | -17.059401 | -56.759102 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e94731c-8c66-3fff-90a2-1ee6fc7bb470 | -17.061001 | -56.766399 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8d51a3a-3dde-3355-a8dc-164fe9ec811c | -17.062599 | -56.773701 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c8bd5f6e-a86f-38ed-9b17-0e8caacf6d89 | -17.192801 | -57.376598 | 2024-10-02 01:23:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b72da1de-b3fc-39a6-ac95-16ab7850e579 | -17.194401 | -57.384201 | 2024-10-02 01:23:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e401e81-8554-3e22-a789-c4a059863229 | -16.841499 | -55.817402 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 19deca4a-7954-30cb-a86e-1b61b294c5a2 | -16.8431 | -55.8246 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 48d17408-97b8-353b-a561-cd4b87394255 | -16.8447 | -55.831699 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 816ac77a-1d3e-3279-bf43-6a82734e9592 | -16.8463 | -55.838902 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 575ffe15-79ec-36eb-b53d-b75b08b96a67 | -16.8479 | -55.846001 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 283d14d3-6478-311b-8aff-70b65c18f862 | -16.8575 | -55.888802 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4d1fa80-d16a-3b1a-9d6f-0e5a0ecb2e30 | -16.8591 | -55.896 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfc46f92-da4e-3684-9001-780fac3940cf | -16.8606 | -55.903099 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5e394ce-fa33-38f1-b52e-fde061d16f78 | -16.8622 | -55.910301 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42ff3214-49a2-32e6-95fe-bbf7e24c5cb3 | -16.8638 | -55.9174 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44a8fbf9-4ab5-3fb3-bf2a-108a17094eaf | -16.8654 | -55.924599 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c6331e30-42a1-313f-9cd5-541d6a54973f | -17.040001 | -56.7174 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 08efd23b-64e3-3e69-9ecc-da5c5c560c20 | -17.041599 | -56.7248 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1496f55-7520-3dc7-aa16-c48fb26e624e | -17.0432 | -56.732101 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d4616b3-c58d-3a2c-89be-20c9ea3680fb | -17.0448 | -56.739399 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c0013a4d-f4e1-3969-83e1-9b20c7b11184 | -17.0464 | -56.7467 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1fe78051-e295-34d7-8d31-349aebd9958d | -17.048 | -56.754002 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae50a7e1-d009-302d-b553-112a92843eb5 | -17.049601 | -56.761299 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7e2ca56-a0ee-3df8-a768-c9665695c78f | -17.051201 | -56.7686 | 2024-10-02 01:23:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32092d8a-b633-35d3-8a19-84da4368291c | -17.1847 | -57.386398 | 2024-10-02 01:23:53 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15deb230-218e-3454-b6c6-ba7b540e0274 | -16.8445 | -55.8769 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50ce0996-69ce-3a9e-8893-1856b94bd052 | -16.8461 | -55.883999 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4845d799-7e59-32e9-b5d1-83fe93daa63f | -16.8477 | -55.891201 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2de7da43-3400-300a-b415-68a98857534f | -16.8493 | -55.8983 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9906519-fc6c-343a-bbf7-a7857b7de75d | -16.8508 | -55.905499 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 528dd372-ac29-353d-9337-867dfc0d0acb | -16.8524 | -55.912601 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0431ad7e-8c42-3fed-8804-e7b6859fe5cb | -16.833099 | -55.872101 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40b130c0-2df1-3417-9d88-55fb4a6c46a3 | -16.8347 | -55.8792 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| caaa3447-8424-3ac3-acd1-839df705a605 | -16.8363 | -55.886299 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0808210-902b-32fb-9779-abf5b4440bd0 | -16.8379 | -55.893501 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3f7d3445-fda0-331c-a7c1-fafe38adbd4a | -16.8395 | -55.9006 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0590d599-d26e-3d80-8576-7f2bd91bfb0e | -16.841101 | -55.907799 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9dc8cdd9-b7b7-31a1-9201-a2e50530fd8f | -16.8522 | -55.957802 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1540bada-97ab-31ed-ba9a-9cc13da9974c | -16.8538 | -55.964901 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de31a15b-6eb7-3afb-a6f3-87f63b9f3756 | -16.804199 | -55.7887 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38be15e1-37ce-343d-99d7-3513e706fea0 | -16.823299 | -55.874401 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d75b9b12-3c69-38e4-bbc9-8dc5318b9d9b | -16.8249 | -55.8815 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c2c4cb7-ea4b-34b0-a826-ba258d3d6e08 | -16.8265 | -55.888599 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 980a1653-ee40-39df-b495-efee64fa61f9 | -16.8281 | -55.895802 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fabf7ccd-426c-30da-8ef8-08529e95591c | -16.8297 | -55.902901 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 725837c6-79f2-3aa1-90c2-910ea07b9df5 | -16.831301 | -55.910099 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0778736f-d8e7-3496-a32f-d51b3d861d04 | -16.832899 | -55.917198 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f95fe56-fa26-30e3-bfd1-9e31b0ad447f | -16.8424 | -55.960098 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bab6d823-a2df-31fa-b8ce-fe255e35d4b9 | -16.727301 | -55.491501 | 2024-10-02 01:23:53 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64b3db82-ae64-314d-a11d-8108e23ca5ff | -16.794399 | -55.791 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d818624-df91-3e8a-b8f5-4ac96c9981da | -16.811899 | -55.869499 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77bcbca2-e97d-306f-afce-d6e8537b8798 | -16.813499 | -55.876701 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b789eb10-15f1-37e1-af18-4b02cc1dc24e | -16.8151 | -55.883801 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8e4606c-561b-35dd-8594-6c1265b9f240 | -16.8167 | -55.8909 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6408a95b-c8d0-3bb3-8e0b-f238dec59b0b | -16.8183 | -55.898102 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 458cb305-93cb-3c35-b857-e25bebb49225 | -16.819901 | -55.905201 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f19949c-609c-3937-b95b-872c5effb1ab | -16.821501 | -55.912399 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a80e55cb-0e7c-3c66-bae8-a8e79c20336d | -16.823099 | -55.919498 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba97105d-9743-3c87-8a76-9b0d2c8a0ed7 | -16.8326 | -55.962399 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 830f3d1a-c0d4-39e4-ad8d-18125d8c5c34 | -16.8342 | -55.969501 | 2024-10-02 01:23:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4a2f079-357c-3725-8eb6-565cc5c52160 | -16.717501 | -55.493801 | 2024-10-02 01:23:54 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d9ac236f-760f-3aa2-86d0-3b6e76be006c | -16.7815 | -55.779099 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01355c8d-f749-39aa-a033-3871ceaaacb6 | -16.811701 | -55.9147 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf17a790-671c-3446-b0b3-ffd8afb6d6a3 | -16.813299 | -55.921799 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d727bb8e-b946-38c1-a90e-5bbbe6263339 | -16.814899 | -55.929001 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e36b9f8-657f-3b71-b7b1-14ac0aa76cf4 | -16.822901 | -55.964699 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5f89f7fe-2027-364c-99e5-96e2cbe12d97 | -16.824499 | -55.971802 | 2024-10-02 01:23:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README24.md)
