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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7694b5f2-214e-32e4-a146-3da157bac416 | -16.9998 | -57.4586 | 2024-10-13 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| e6ba96d1-a4d0-36fb-b660-8bde50ecf6b4 | -17.0001 | -57.4381 | 2024-10-13 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.4 |
| e1b93e35-c3a9-3dd9-b485-d3859e6a9c1b | -17.0004 | -57.4176 | 2024-10-13 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 424a48f5-fa02-354b-9b08-f1ca22d2f694 | -17.0194 | -57.4563 | 2024-10-13 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| c76d077d-2a73-3667-a7c0-4a61c4b552cf | -17.0197 | -57.4358 | 2024-10-13 07:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.1 |
| 8f0a1c2e-23d8-3a83-a4db-71cb40cc0414 | -17.1758 | -57.479 | 2024-10-13 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 8debc980-c0c6-307e-b933-007145a9dddb | -17.1761 | -57.4585 | 2024-10-13 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.7 |
| b0c26ce3-ce01-33ee-ae68-37c64cdffef5 | -17.1954 | -57.4767 | 2024-10-13 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 5931c84a-303f-3cbd-a7f4-b95f523c591a | -17.1957 | -57.4562 | 2024-10-13 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.7 |
| 0f7a3ea3-a3f5-398e-a600-23618114640e | -17.196 | -57.4357 | 2024-10-13 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 6e807f8e-cdd1-30a8-b9c9-f7833955edaa | -17.6474 | -56.2876 | 2024-10-13 07:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 164.5 |
| 098d072e-b38f-3030-844b-f25b7882de25 | -17.6478 | -56.2668 | 2024-10-13 07:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| a40c2819-c5ad-33d8-91d7-d58a8de225b8 | -17.6672 | -56.2851 | 2024-10-13 07:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| d4e5e1c9-0d60-3372-8d10-90482004a214 | -17.9643 | -57.3637 | 2024-10-13 07:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.6 |
| ab3d1d36-a542-3cce-9b10-a46c023d1d57 | -17.9841 | -57.3612 | 2024-10-13 07:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.1 |
| a8c23bce-4734-3644-afea-9b50c5da81ed | -18.2155 | -56.5457 | 2024-10-13 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 57f9daa9-f243-3c66-8a9c-4b8585f7d021 | -18.236 | -56.5014 | 2024-10-13 07:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 038ac0a3-7a48-3a69-83b6-5d78b28f2c41 | -17.9 | -57.36 | 2024-10-13 08:03:45 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eab7960a-aa5c-39fc-96c1-3f05cedb8168 | -12.4792 | -63.0159 | 2024-10-13 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.6 |
| cfd02586-2dcf-3a9a-8f23-0792684bb829 | -12.4794 | -62.9967 | 2024-10-13 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 2e2cb6de-ff39-32aa-8691-ab5c24ef9f15 | -12.4981 | -63.0148 | 2024-10-13 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| fa397291-89cf-3dae-a612-414182eb2966 | -12.4983 | -62.9956 | 2024-10-13 08:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 38a56a13-ab43-3c32-983e-685c48b29a0c | -17.0197 | -57.4358 | 2024-10-13 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| b9bdd93f-9cc3-38de-b266-f63fce895516 | -16.9995 | -57.4791 | 2024-10-13 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| af2459f9-6a9e-3343-a782-16f6be9e796b | -16.9998 | -57.4586 | 2024-10-13 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 9d54b918-10c5-3641-85d2-9728be34c34e | -17.0001 | -57.4381 | 2024-10-13 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.4 |
| 433c55a3-ead8-3bb3-9b2b-9c5c70358c46 | -17.0004 | -57.4176 | 2024-10-13 08:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 679c8708-92ff-317d-a401-50fef6e9c09d | -17.1764 | -57.438 | 2024-10-13 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| 85ac1753-a179-3785-9cc2-2d98a4fdefd6 | -17.1761 | -57.4585 | 2024-10-13 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| bd15983a-ecd9-3ed0-8d67-03d3f9aaf026 | -17.1758 | -57.479 | 2024-10-13 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| d72f6b8d-7f23-3fec-8119-c2ae6b1e8372 | -17.1957 | -57.4562 | 2024-10-13 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.7 |
| 7ae19f96-f068-3955-a04b-ea3a15143050 | -17.1954 | -57.4767 | 2024-10-13 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.0 |
| 1a75bed7-8f01-3bfd-944c-32e726c7fbc7 | -17.6474 | -56.2876 | 2024-10-13 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.8 |
| 4f305434-d092-39d1-9bdb-ee1091877028 | -17.6478 | -56.2668 | 2024-10-13 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 843c4266-b284-3987-95e8-67d6c856a193 | -17.6672 | -56.2851 | 2024-10-13 08:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| dd2933f5-9e9e-370d-9832-f5997a15d845 | -18.2151 | -56.5665 | 2024-10-13 08:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 1ffa6aa4-8f01-3c61-a7cc-1ffc9f532fe5 | -18.2155 | -56.5457 | 2024-10-13 08:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| d2936dbb-620a-307e-ae80-6deea18595a4 | -18.236 | -56.5014 | 2024-10-13 08:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 77d29d73-6df9-364b-938c-e9b5b3783603 | -12.4792 | -63.0159 | 2024-10-13 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 16484767-4050-30d4-a9d2-43e20de6d69a | -12.4983 | -62.9956 | 2024-10-13 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9389fee1-d28d-38a4-a7aa-229b5e71aa8a | -12.4981 | -63.0148 | 2024-10-13 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 8e1d008c-d7dc-3f31-9d9a-ad7d30833783 | -12.4794 | -62.9967 | 2024-10-13 08:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c3e8f75b-f459-3b11-978a-a6201eb84917 | -16.9995 | -57.4791 | 2024-10-13 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 4f3f2749-0bef-3053-bfb1-a8adaa697027 | -16.9998 | -57.4586 | 2024-10-13 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| cee2f714-1f2b-306e-96db-de66dfeb62c2 | -17.0001 | -57.4381 | 2024-10-13 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.0 |
| 9edffaee-1bfa-337e-a70d-81f726e30d69 | -17.0004 | -57.4176 | 2024-10-13 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| eb15f551-23b9-3a11-bc0d-0751b407e2ee | -17.0197 | -57.4358 | 2024-10-13 08:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.3 |
| cef5fa39-cafa-3b2b-b7b3-3037bdeb1c19 | -17.1758 | -57.479 | 2024-10-13 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 7dca3343-c797-3ce6-817f-46ca6234c208 | -17.1761 | -57.4585 | 2024-10-13 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.8 |
| afcf4ed4-21c6-37e7-8ceb-d5a93b8e25e6 | -17.1764 | -57.438 | 2024-10-13 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| fae3994f-01e3-36c5-8bcd-20cca359140e | -17.1954 | -57.4767 | 2024-10-13 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| 82d2123d-95f0-3b07-838f-f0c42e8a7776 | -17.1957 | -57.4562 | 2024-10-13 08:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.5 |
| 890788c4-53b4-3123-a44f-91c5a442fbe3 | -17.6478 | -56.2668 | 2024-10-13 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 748753bb-ef3a-3ea9-b64c-9f7dd49a5782 | -17.6672 | -56.2851 | 2024-10-13 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 59032e96-9473-351f-9dec-f2006be199c0 | -17.6474 | -56.2876 | 2024-10-13 08:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.3 |
| 59e019a5-04bc-3cb6-8046-5c1d2e49d8c5 | -18.2357 | -56.5222 | 2024-10-13 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| be0bc6b6-623b-336b-854e-bda9bc8fe121 | -18.236 | -56.5014 | 2024-10-13 08:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 90fd6f28-eb3b-3c31-890a-0c109240ff20 | -9.8364 | -60.3169 | 2024-10-13 08:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 374c1af7-37c6-35b5-b5fb-3f319414d819 | -17.0004 | -57.4176 | 2024-10-13 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 5ab710d9-3e19-39e8-a2f0-f660b4ae71ef | -16.9998 | -57.4586 | 2024-10-13 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| b2319822-7ff3-376b-97fc-c08b7a0cf745 | -17.0001 | -57.4381 | 2024-10-13 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.9 |
| 7212c231-089f-34ae-a0ca-6d79027a4994 | -17.0197 | -57.4358 | 2024-10-13 08:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 8926002f-fb1d-397a-ac28-64533cabd2fd | -17.1758 | -57.479 | 2024-10-13 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 2c39c3f5-09d0-3c91-8ae2-5b95ad73b15e | -17.1761 | -57.4585 | 2024-10-13 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 6949ff6a-dd04-31fa-b036-2538e83432eb | -17.1954 | -57.4767 | 2024-10-13 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 13d56d62-b2a0-3369-95ae-178ddd32934b | -17.1957 | -57.4562 | 2024-10-13 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.1 |
| 7b154338-b7c9-3137-96a5-807d7f154aaa | -17.196 | -57.4357 | 2024-10-13 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| fe9d0098-4a9f-3ee7-8225-0d25dc79fae2 | -17.6474 | -56.2876 | 2024-10-13 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.4 |
| 8a7a2b03-99e3-3a3e-b807-6550e521f663 | -17.6478 | -56.2668 | 2024-10-13 08:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| a1ab7135-2ea4-3be9-8390-74925e418aa4 | -18.2151 | -56.5665 | 2024-10-13 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 6cdd465b-fb36-3e5e-9e4f-b00a2832aa71 | -18.2155 | -56.5457 | 2024-10-13 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.4 |
| 79d440f1-8eb0-315c-90dc-06a00e091b04 | -18.2357 | -56.5222 | 2024-10-13 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| c1dd4089-3ae4-35d7-bfc0-0b32042a46ea | -18.236 | -56.5014 | 2024-10-13 08:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 6451d478-84a8-3743-b615-5ea853272718 | -9.8551 | -60.3159 | 2024-10-13 08:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 7b861953-c9fc-3060-b169-30f64d8f0a9e | -9.8364 | -60.3169 | 2024-10-13 08:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b0d89558-2864-3d74-ae32-4536ab1baf9d | -12.4792 | -63.0159 | 2024-10-13 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 8ab7e4b6-789d-353f-9d07-c2dfe2dd4c76 | -12.4983 | -62.9956 | 2024-10-13 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 556378e7-d0d5-3255-b485-e2cfafdd73cb | -12.4981 | -63.0148 | 2024-10-13 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1b3e45f9-10c1-3148-8e4d-bb6c7185dcd3 | -12.4794 | -62.9967 | 2024-10-13 08:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e88efdb9-88ac-3467-85e9-65b0c9d59192 | -17.0197 | -57.4358 | 2024-10-13 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 43d05e0f-91bb-3d35-9330-e9b03d8efc30 | -17.0004 | -57.4176 | 2024-10-13 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 8b509c27-a7d4-30d3-9667-3dd4d126f9f7 | -17.0001 | -57.4381 | 2024-10-13 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| e3ba813f-3a7c-38fd-8c19-0cb22100e9b6 | -16.9998 | -57.4586 | 2024-10-13 08:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 877b33d0-a741-3b3a-a1f8-c1e217933ca2 | -17.1957 | -57.4562 | 2024-10-13 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.7 |
| ace26cce-5036-3b85-a99e-47099c66e2d5 | -17.1954 | -57.4767 | 2024-10-13 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| c6afd8a7-d370-3138-9d00-38829aff567b | -17.1764 | -57.438 | 2024-10-13 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 592b5f7f-09b9-35c3-bc74-387d9c2e509d | -17.1761 | -57.4585 | 2024-10-13 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 97ce414f-613a-383e-83a9-d88b796768b4 | -17.1758 | -57.479 | 2024-10-13 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| f33b1252-76fc-3a7e-9ca3-a25c82339237 | -17.6672 | -56.2851 | 2024-10-13 08:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| fb51d8ee-a975-3b7c-86fa-4cea10fba63e | -17.6478 | -56.2668 | 2024-10-13 08:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 546819f4-fc7e-33f7-b38f-09a93342a33d | -17.6474 | -56.2876 | 2024-10-13 08:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.7 |
| 33fb15f4-e0e1-3576-9cf0-0cd7d69882cf | -18.2357 | -56.5222 | 2024-10-13 08:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 1a4c56e8-9baa-3033-9ce0-ca174460c0b4 | -9.8364 | -60.3169 | 2024-10-13 08:46:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f6599522-ab41-3205-9da3-ff1618c1ac91 | -9.8551 | -60.3159 | 2024-10-13 08:46:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| bea87fd5-db34-3e2e-9684-80840eae16a9 | -12.4792 | -63.0159 | 2024-10-13 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.4 |
| c758d1e2-8b73-3ac3-88c2-86b261bb3cac | -12.4794 | -62.9967 | 2024-10-13 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 34450f0c-4b0e-3f10-8ea5-1731a159987f | -12.4981 | -63.0148 | 2024-10-13 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 22915ece-66ae-3f20-ae1d-34c9a5c0a66a | -12.4983 | -62.9956 | 2024-10-13 08:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e47a1aef-fd27-3594-88c6-e2c6a37bbdcc | -12.9372 | -62.5275 | 2024-10-13 08:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4360ea00-cc52-3568-98c0-bfb2d4c66ab7 | -13.0133 | -62.4843 | 2024-10-13 08:46:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |


[Clique aqui para ver as próximas entradas](README116.md)
