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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c974b6a-b729-3b0d-bf5a-2f3440ca705e | -11.0802 | -54.0302 | 2024-10-07 14:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| b310c7ef-3bc0-387d-b5c3-1310553fb53e | -11.9862 | -50.1787 | 2024-10-07 14:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a07435c3-71c9-38f1-b8e6-f901a2c41eb0 | -11.9671 | -50.181 | 2024-10-07 14:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b0cba530-2ec0-3d8b-843d-906afccd7bd7 | -14.0382 | -45.1414 | 2024-10-07 14:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| ea0fa3fc-d955-3b98-9f9a-0638ccad6b9d | -14.0188 | -45.1448 | 2024-10-07 14:36:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| a5bdd8cb-8d88-3995-bf4d-95c37d124807 | -15.0422 | -51.24 | 2024-10-07 14:36:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| ab46a642-e45d-39ec-8635-2c37fe2b84be | -15.0426 | -51.2184 | 2024-10-07 14:36:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 600d17a8-ddff-3a6b-9d26-79f0373b2b4c | -16.9092 | -47.1724 | 2024-10-07 14:36:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 6cb9824c-d932-3cb2-aff0-d29e56d01471 | -17.6679 | -53.0819 | 2024-10-07 14:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 152.5 |
| d38dbb14-d995-39cd-993c-be1e0af39b73 | -17.6684 | -53.0604 | 2024-10-07 14:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 1d65ba61-67c6-383d-a14e-67e518ec2398 | -17.7728 | -53.7705 | 2024-10-07 14:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 227.5 |
| 39a5e41e-13f9-33f5-8aaf-57e593c9e2d8 | -17.7926 | -53.7675 | 2024-10-07 14:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 88e0287f-0c9f-3cf7-95ba-e7632cb3cd4e | -17.7468 | -53.0911 | 2024-10-07 14:36:46 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 7cbfb30a-1e18-3a9a-958a-da86c82e3a29 | -18.301 | -47.1425 | 2024-10-07 14:36:48 | GOES-16 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 79053076-1ebb-33d7-bdb6-c560b0b4ecb5 | -19.1995 | -46.5714 | 2024-10-07 14:36:53 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2793d7ef-bc0a-3e5d-b564-58bd5aaad64a | -19.671 | -56.4709 | 2024-10-07 14:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 159.8 |
| 1e7da7f5-e74e-3e46-81e9-6bf6912d0a8b | -21.4152 | -57.2472 | 2024-10-07 14:37:05 | GOES-16 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 103.0 |
| b6212a4d-2fb6-35e6-923b-70cc73d69525 | -3.1975 | -42.4842 | 2024-10-07 14:45:24 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c0ab2362-2fc3-3542-9c04-cd4624186356 | -3.3093 | -42.5263 | 2024-10-07 14:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 881961d7-7d60-339d-8504-8d3a4658c969 | -9.5259 | -50.1851 | 2024-10-07 14:46:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c7528fcd-cafe-35d2-ae30-207d15926d5d | -10.6688 | -50.7529 | 2024-10-07 14:46:07 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 5d0d4ec0-1ebd-3ae6-a9da-509bf514d297 | -10.8032 | -53.5417 | 2024-10-07 14:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| c8b4efad-f9c2-379f-9718-ef213ffa2755 | -11.0991 | -54.0285 | 2024-10-07 14:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 233.2 |
| 06dabc37-e3bc-3038-8ff6-9d8db7b5583a | -11.0802 | -54.0302 | 2024-10-07 14:46:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 55a8e6b3-da17-3526-937d-367571581e0b | -11.2768 | -46.8424 | 2024-10-07 14:46:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0a6c0258-bc63-3ed2-a7b4-103798d5f37f | -14.0582 | -45.1146 | 2024-10-07 14:46:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| cc104b0e-361a-32ad-9e3f-c0a28b6d21a7 | -14.7935 | -48.05 | 2024-10-07 14:46:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 441e1c6b-67e0-3608-8623-0e3c73213773 | -15.0426 | -51.2184 | 2024-10-07 14:46:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 14408cab-7ba7-38cd-9091-df8f5384984f | -17.6684 | -53.0604 | 2024-10-07 14:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 331601e9-cadb-3563-9698-40d135e394a4 | -17.7076 | -53.0757 | 2024-10-07 14:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 0db3aa67-2e1a-30d2-9b78-19a5eb08f88d | -17.6679 | -53.0819 | 2024-10-07 14:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 5e69ec4e-8d43-3190-86d3-b50d6a76fd90 | -17.7666 | -53.088 | 2024-10-07 14:46:46 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 461.5 |
| d68384f4-18b0-3c75-8ee2-47e18d20535b | -17.7926 | -53.7675 | 2024-10-07 14:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| f3729bbc-aaaa-3d2b-bcc4-557080f0f192 | -17.7728 | -53.7705 | 2024-10-07 14:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 8b7553f8-16b8-38f4-a46f-a91a3a09d841 | -19.671 | -56.4709 | 2024-10-07 14:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 163.6 |
| 07fd490a-9a72-37fe-b17a-e779db631caa | -21.4152 | -57.2472 | 2024-10-07 14:47:05 | GOES-16 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 96.9 |


