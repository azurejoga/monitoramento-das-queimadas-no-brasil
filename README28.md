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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5f1a013-25b2-3e02-b5a5-140b7e404136 | -19.58976 | -56.71368 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 53896d46-22e8-380c-a365-751a9b313703 | -19.51084 | -56.5904 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d1de8e65-44b8-3fc3-a48a-48abc6b1de75 | -19.50985 | -56.59535 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| f1e97623-1779-35b4-a022-b58b0ef326a9 | -19.5011 | -56.56761 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f455feff-a262-3235-8842-c621f5ec979a | -19.49912 | -56.57747 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b22db185-2443-38e3-9f43-914f5f0d8f4b | -19.49018 | -56.62198 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 133ebdc7-32ba-3f51-94cb-ffe5dd710c56 | -19.48917 | -56.62695 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ade4db63-684f-32d7-a76b-f948e8883c51 | -19.58011 | -56.73775 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7dd14220-c400-365c-833a-575bd0ff7b95 | -19.57964 | -56.76402 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 197d14d5-d714-3aca-9ecf-9aa0b64fb895 | -19.57862 | -56.76908 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a7229b74-2245-35d1-b885-13642ee285ea | -19.57754 | -56.72667 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6b7bb037-f73f-3cb9-9f0e-c7de9afda695 | -19.57037 | -56.71454 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7f1a3a18-7d4a-3536-882c-f844d71352fd | -19.56679 | -56.70849 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7cebdf87-1903-347a-967e-eb4ab6b0e4b1 | -19.56577 | -56.7135 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 2ad0457d-636e-389d-ab35-87b299ee9863 | -19.56445 | -56.70657 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 997da618-e508-34fb-bd39-c9f9141f7f01 | -19.56321 | -56.70245 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d59ca13a-7258-36f8-80fd-3d9bb7477e74 | -19.54112 | -56.72757 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 6a876325-971b-34d5-b630-12a21391105b | -19.54074 | -56.71838 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| dbb50fbf-babf-3ad2-b341-ae11361eedc4 | -19.53971 | -56.7234 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 82a09e54-f7fe-3022-9de7-048b1f345cb3 | -19.53868 | -56.72843 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 013f0b1f-fd04-3143-a46b-619bd57b3123 | -19.53652 | -56.72652 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 87d0bf56-024b-37b0-8f2a-6e7b074bb7f8 | -19.52308 | -56.69723 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 780fa67d-5472-3cd9-b254-4c5e23f49892 | -19.5211 | -56.70727 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4d0520ea-1a89-3930-87ab-2ed938074313 | -19.5083 | -56.69913 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 43452711-7ff7-3b1c-807f-40de35f70080 | -19.50825 | -56.57951 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2eae016d-4d96-325d-b3e6-5e0362753477 | -19.5073 | -56.70414 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| 959bfa6f-6265-32dd-bfa2-8c3d5dbd9adc | -19.5027 | -56.7031 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| d0a26846-6a5f-3891-b4c6-b0335a5fb146 | -19.5017 | -56.70812 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| e7a421ed-af59-3b7e-bad1-381f28fe3429 | -19.50011 | -56.57254 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ca8a9791-fbd2-3cb4-8a2d-b0fb34fff8c1 | -19.49972 | -56.59824 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 5e1020c2-9bbd-3ad6-a933-d100f9e16bc5 | -19.49615 | -56.59227 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d4a9fba8-4848-3a20-a0a4-4c722b07e095 | -19.49509 | -56.71714 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3bad074a-11c0-3834-9e8b-8c6989732dfc | -19.4925 | -56.70605 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5a91ecdd-72a5-3ad2-b25b-77021798d312 | -19.49058 | -56.5962 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 05073fdd-ef43-3063-996a-02abd186ea85 | -19.48675 | -56.66288 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 81c2481f-3f66-3297-bc54-186c5e3307e8 | -19.48588 | -56.71508 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cb97ebff-572f-3f25-bc0b-3ffa56b949ac | -19.4846 | -56.62593 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1b2d2093-747d-30d5-b494-b7a34a91c7f4 | -19.48216 | -56.66183 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 607e0349-33c3-3c40-a6f6-cd4185a15f02 | -19.48127 | -56.71404 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 881a0fe1-3622-381f-a15c-ea5efb1dea02 | -19.47914 | -56.67683 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1da90fb3-9db1-3184-9c7a-6c25ffbd0a37 | -19.578 | -56.70055 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 07a2f1ab-9d2c-3f96-a620-b87a79653d99 | -19.57395 | -56.7206 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 68562ec3-fbf2-31ed-957f-a374cfb58ea9 | -19.56882 | -56.69848 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cad86d78-37de-3fe0-9d87-6a883fd8818f | -19.56781 | -56.70349 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fb7aa36c-f767-36dc-b344-ef36ffe9b862 | -19.56476 | -56.71852 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| bb79105d-a02a-3b76-a91c-4f91e1ef355a | -19.56347 | -56.7116 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 4ccc048e-dbed-32df-b7ab-ae1d7e020eb6 | -19.56016 | -56.71749 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b66a583f-2210-3cdf-b117-166516b3d7a5 | -19.54409 | -56.71246 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 59c89e08-855b-3d0f-a1d1-505912a69e7a | -19.54279 | -56.70835 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9ff30da5-ff40-362f-804c-2e0d059d69af | -19.53949 | -56.71143 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c0e39c8e-dbf5-3cf6-9c27-55c7de7c532a | -19.53489 | -56.71039 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 9d300a1f-0d3b-33c4-9039-b731aa4b58d6 | -19.5339 | -56.71542 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| f7ec674f-3327-3107-97cc-bef8ba69204c | -19.53029 | -56.70935 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ac6b2056-d231-3289-8589-e4a18988562d | -19.52669 | -56.70329 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1a08bd62-94c7-3f8b-b027-ce405bf36c15 | -19.52408 | -56.69222 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2134979b-3ae1-35ad-963d-b8dc4d81fc8f | -19.5237 | -56.71837 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d3af49d0-45f8-3449-89eb-ada6dadfaace | -19.5129 | -56.70017 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 250ec4d1-67d8-3a26-a090-68546ad8897e | -19.5103 | -56.6891 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ba158c35-0b73-38b5-858f-9899ed260240 | -19.5093 | -56.69411 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 73b81eef-5e28-3975-aad1-64ec331657e9 | -19.5063 | -56.70917 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.3 |
| b028c548-2cb1-31ff-8829-652ab2be9e6b | -19.5047 | -56.69307 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 5a1d7db1-5f13-3ee5-b7b5-be41d77a4f71 | -19.50011 | -56.69203 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8ec6dc63-e634-385b-b91d-3ad7a2c07d40 | -19.4971 | -56.70708 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c877b0ef-d189-37dd-a9b1-9102df9b609e | -19.4961 | -56.7121 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4393ae8e-4b6f-37b3-bab1-1e2dc45afeeb | -19.4935 | -56.70103 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7f644c1a-9882-3f73-9eea-b2bd6bf01dd7 | -19.49149 | -56.71108 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e9c2709a-e7cf-3bb8-aaa1-b88da815794e | -19.48487 | -56.72011 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 4b01a804-f7a5-31c3-88a2-523e7c919a99 | -19.63148 | -56.69698 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 39aa30cb-e746-3976-84c2-f7d52dfd2f1f | -19.6295 | -56.70698 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 6c38b24b-71b3-3be2-b28a-f657eed36bab | -19.62689 | -56.69593 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 96dc64c9-b558-3c1f-b086-9ede6e371111 | -19.62491 | -56.70594 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 31b63310-2543-3492-a266-e09a76269ceb | -19.62131 | -56.69989 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 87f72d9b-df55-3972-b86c-4830f82a9848 | -19.62032 | -56.70489 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 69904a2c-0997-3a1d-977f-35b776067a48 | -19.61832 | -56.71491 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 2714f4d4-2167-35a7-b6c8-5198cb7ae39a | -19.61373 | -56.71386 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e0961bef-893f-3dad-ae5d-35db2cf61830 | -19.63219 | -56.64513 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 204c6b7f-e50c-3108-b8a4-483658bb4d03 | -19.63121 | -56.6501 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| edec82e5-6b30-3ed8-a2a0-d1afd004f485 | -19.6285 | -56.71198 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b2d0223f-790a-34b3-81e6-dcd3ca554288 | -19.62788 | -56.69094 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8ca5986f-43f5-3a45-a522-661d00cba7c3 | -19.62762 | -56.6441 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 790f0422-91b1-3e2f-839d-69386272f1a7 | -19.62391 | -56.71094 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 4d905987-46b2-3c4a-8adf-27e1d4f17a37 | -19.6223 | -56.69489 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| bf7049cb-c2d3-316e-aa87-1b9461f7b777 | -19.62093 | -56.72596 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a2e7442d-ddc3-39d9-9fc6-959e5ce9d57c | -19.61993 | -56.73098 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 17fa5ba3-6444-3db4-8a21-2a040ace41fb | -19.61733 | -56.71991 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ed537c42-b545-3350-b3b0-29a282c1cc6f | -19.61633 | -56.72492 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a3130e73-0979-3066-b530-a8659d20ece8 | -19.61573 | -56.70385 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ef010561-8aaf-3546-8efa-5b76c62edf86 | -19.61534 | -56.72994 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a8704705-1ab2-3eb9-bc13-7eb02f083b18 | -19.61433 | -56.73497 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 202fa0b7-eef5-360d-af54-d31833050cff | -19.61333 | -56.74 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| be547fb5-ee0d-3c39-8cf4-2d97a7d2380f | -19.61074 | -56.7289 | 2024-10-31 04:29:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| de726ec4-1cbf-3aa5-b580-74f72bf51854 | -19.54508 | -56.70744 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6d288996-faa4-3c8f-ad64-3b4a8d35dff3 | -19.5431 | -56.71749 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7642f2aa-9c7a-3a45-8c0d-43e9fb5d11af | -19.54048 | -56.70641 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3a2f4271-a1db-32dd-942e-30cb0d734186 | -19.53751 | -56.72149 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.8 |
| 00b73fb3-d2fe-399a-a258-604c2af0a97c | -19.52831 | -56.71942 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 9621209a-9f27-35d1-8907-a895d8143c55 | -19.5247 | -56.71334 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 23f0d0e5-9166-3cc0-a267-e8b677134fe4 | -19.5119 | -56.70518 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 2c311c41-b104-3c13-a1b6-f33848b651f4 | -19.5037 | -56.69808 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| c9f24f3e-1b4d-3ad6-82d8-6f133a66e2d3 | -19.50211 | -56.68202 | 2024-10-31 04:29:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
