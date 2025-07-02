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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54d0f607-040b-3107-9f28-93a9909f5096 | -6.8193 | -45.5446 | 2025-07-02 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 1099c03d-1b40-3687-bd3b-ed478935c22a | -12.4274 | -50.0171 | 2025-07-02 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 5b106546-7bc5-3c70-8870-321ad0394a37 | -8.3146 | -55.0961 | 2025-07-02 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| e28c78f0-caec-37a1-8b82-2f2a49329f5e | -6.9605 | -42.8816 | 2025-07-02 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 117bb2fa-a4f3-3cf3-820a-29b75ee575ef | -12.6632 | -45.3008 | 2025-07-02 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 6771d134-7a51-3216-ae4b-f3bf677c3b05 | -12.4274 | -50.0171 | 2025-07-02 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 8dc5cffc-ad90-3b57-a3d6-d692547ed489 | -12.427 | -50.0387 | 2025-07-02 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 4321aefd-9721-35ed-9468-51cbfc3da173 | -9.9761 | -46.1725 | 2025-07-02 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a2afe255-636d-3f5c-93d1-bb1814e92c9b | -6.9605 | -42.8816 | 2025-07-02 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.2 |
| 0f8ada0a-df64-3b31-a328-cb2894622de1 | -7.6051 | -45.7464 | 2025-07-02 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| d7a10ae8-4189-3fef-8b10-28c1f0ef2f03 | -11.1666 | -49.0428 | 2025-07-02 14:10:00 | GOES-19 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| eadd5be3-dfb6-35a1-a832-7c22f562dbc1 | -7.6239 | -45.7447 | 2025-07-02 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 42669aa8-9754-30f1-a962-f2669c46c87d | -5.9216 | -43.4403 | 2025-07-02 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| c07b0bac-add4-3fb5-98dc-9bb98f5e536f | -7.6051 | -45.7464 | 2025-07-02 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 3d2bdea4-efea-30fb-832a-4f882a25e3e0 | -9.9761 | -46.1725 | 2025-07-02 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| b27767a4-b173-37b3-8b6b-2e6e34d53ecd | -12.4274 | -50.0171 | 2025-07-02 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 225.2 |
| ece33d08-bfd9-3e7b-8c9a-791d253dbb98 | -7.6239 | -45.7447 | 2025-07-02 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 15922093-2563-3332-894f-406815613d4d | -12.6632 | -45.3008 | 2025-07-02 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| d517217f-3875-3901-a31f-4786f30851ef | -6.9605 | -42.8816 | 2025-07-02 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 205.1 |
| f390c6f5-a377-3393-8920-9db0756b679d | -12.427 | -50.0387 | 2025-07-02 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 180.5 |
| cfbca44d-9f5b-322f-8b80-8f6ccc6ef5f2 | -12.427 | -50.0387 | 2025-07-02 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| e4c2f039-68b1-317f-9fa5-b7afa9d120b1 | -7.6051 | -45.7464 | 2025-07-02 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 08505be5-5969-3597-8fcc-a54f0fe34cd4 | -7.6239 | -45.7447 | 2025-07-02 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 246861d8-9624-31cc-a10d-0e907b70ba71 | -6.9605 | -42.8816 | 2025-07-02 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 174.2 |
| 7e222911-edb5-3acb-83e6-56ed906b18ba | -12.6632 | -45.3008 | 2025-07-02 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 8a4a304d-71f9-3e8b-b4b8-1c46b6ce56c9 | -12.4274 | -50.0171 | 2025-07-02 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 0a60d17b-edc8-340e-947f-0523a424c04c | -5.9216 | -43.4403 | 2025-07-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 11f202bc-9ec5-3e2e-8eda-768db9ca7bb2 | -6.9605 | -42.8816 | 2025-07-02 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.0 |
| 99db4413-48ff-361b-8841-be04bda64936 | -12.4461 | -50.0363 | 2025-07-02 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 9638139a-ef19-3d47-912d-716b5cac8d90 | -7.6239 | -45.7447 | 2025-07-02 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 86e3f15c-2fef-3560-997b-43fcd18edf78 | -12.427 | -50.0387 | 2025-07-02 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 62f8df56-a3ee-3cbc-9b65-5949c9fb26d0 | -12.4274 | -50.0171 | 2025-07-02 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 6faaf673-e94c-3b95-a5e5-4bbacea1e203 | -5.9028 | -43.4418 | 2025-07-02 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a4211e9d-849c-3ff8-839b-3e01772a8f61 | -12.6632 | -45.3008 | 2025-07-02 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |


