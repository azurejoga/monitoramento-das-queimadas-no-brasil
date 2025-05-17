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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 556a6b90-28dc-3169-9592-7de97274b7f9 | -12.3519 | -49.9617 | 2025-05-17 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| d8c9d51b-8163-3a26-88d2-e45bfb2f4ee8 | -12.4608 | -57.2079 | 2025-05-17 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| d4e3a3eb-bec8-3080-8a00-accae5b9d2b8 | -12.442 | -57.1895 | 2025-05-17 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| a8f1fd96-61d2-33d5-b969-8be2d332b50c | -12.3515 | -49.9833 | 2025-05-17 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 1d308e18-f139-39f7-8feb-e71b3bd5597b | -12.3519 | -49.9617 | 2025-05-17 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 5a2971e1-3995-39af-80ca-4eeb6c7c2564 | -12.461 | -57.1879 | 2025-05-17 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 223.8 |
| 76219f80-3ea7-318f-bf07-1a9ab928721e | -12.3515 | -49.9833 | 2025-05-17 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| ea32d94c-5dfe-3f68-af59-b604baa95852 | -10.8193 | -49.4511 | 2025-05-17 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 47ae1c55-12fb-3ca5-8fb3-c22f570e2a03 | -12.442 | -57.1895 | 2025-05-17 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 05b78d72-7381-3e77-8466-1cc5e3136592 | -12.4608 | -57.2079 | 2025-05-17 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 96f8f306-f056-3aa0-84e0-2844b0507004 | -12.3327 | -49.9641 | 2025-05-17 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4bb0bb9c-0845-37f0-92d2-2fc14fc95740 | -11.2887 | -53.97 | 2025-05-17 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 4662e2fe-fa13-320d-8ac8-cf8177ea3c10 | -12.461 | -57.1879 | 2025-05-17 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 7ca53d70-a381-3fe5-95ea-fdd587fe7aa1 | -12.3519 | -49.9617 | 2025-05-17 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 20b673f3-0ec1-39bd-be45-a0b0d48d0098 | -12.442 | -57.1895 | 2025-05-17 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 31716116-556f-3663-b90e-52d7d2874e11 | -12.4608 | -57.2079 | 2025-05-17 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| bed6c0e8-115d-3c74-b1a6-5da8f75e2115 | -10.8193 | -49.4511 | 2025-05-17 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| cc44efba-fce4-3f2b-9a86-b71edca7aaf3 | -12.3515 | -49.9833 | 2025-05-17 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 7b9bc2c3-37a4-3987-a32d-ee694b7259ad | -12.4608 | -57.2079 | 2025-05-17 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 79623a21-0685-3404-af5a-cfc97988325f | -12.3519 | -49.9617 | 2025-05-17 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 944aa23e-91fd-3f8f-8126-a9bfc89e185e | -11.2887 | -53.97 | 2025-05-17 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 5aa45c88-ee93-384c-9930-5d9f1318ceac | -12.461 | -57.1879 | 2025-05-17 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 6a91673b-f24e-3a9f-8fa2-be1e811e93f7 | -12.442 | -57.1895 | 2025-05-17 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| a1963d52-d6ad-3a9a-84a6-b74664599394 | -12.3515 | -49.9833 | 2025-05-17 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| ec3961e8-b9b4-3e35-8d42-5b83eb704f76 | -17.7652 | -56.3139 | 2025-05-17 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 35cf6824-65d3-3f3c-ac78-955c155dc7d6 | -17.7652 | -56.3139 | 2025-05-17 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 1878ac7a-7cf0-39f1-953e-fa9466f65ae0 | -10.8193 | -49.4511 | 2025-05-17 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| da2d8345-fe41-3536-9a21-34497893420c | -12.442 | -57.1895 | 2025-05-17 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 201822e1-e30a-32c7-af83-6c81e10a1a5a | -12.3519 | -49.9617 | 2025-05-17 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| cf8f857a-a364-31a8-8665-59bc89e468f2 | -12.4608 | -57.2079 | 2025-05-17 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fb9a6aca-2190-3dfa-ae37-2241cb0ce7b8 | -12.461 | -57.1879 | 2025-05-17 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| ae479d39-079a-327d-b20b-4fe76fbbd9e6 | -12.3515 | -49.9833 | 2025-05-17 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 3ef8363c-2eca-35e0-94ca-c0e7c52bbb27 | -11.2887 | -53.97 | 2025-05-17 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| e12fdb42-c85d-3c83-8557-2e0aee87d1c5 | -12.3519 | -49.9617 | 2025-05-17 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 63fc8ded-13b5-30be-8a1d-1aa2313f2746 | -12.4608 | -57.2079 | 2025-05-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5b7f15eb-1dec-3619-8c26-e11b3a7fd578 | -17.7652 | -56.3139 | 2025-05-17 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 2762b4c2-dae9-3b32-aa2a-a68e1ee3d480 | -12.442 | -57.1895 | 2025-05-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| c21e093a-00cd-336b-bd43-eb0e9752ec9e | -12.3515 | -49.9833 | 2025-05-17 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 3a242a08-a105-360e-96aa-d5e705ca36a3 | -12.461 | -57.1879 | 2025-05-17 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.6 |


