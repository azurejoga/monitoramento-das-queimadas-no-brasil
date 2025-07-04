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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00145fdd-2f17-34ff-b65d-1a1c1bfe8db4 | -7.6588 | -44.3515 | 2025-07-04 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| fb93b88d-6aa3-38d5-88ee-038e1774205c | -3.3994 | -43.1316 | 2025-07-04 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 1b1e279b-1d15-36af-9d20-da18bd1fe54d | -10.8161 | -54.0334 | 2025-07-04 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bbd8ea45-8615-3d31-bef0-21a56a551443 | -12.4079 | -50.0411 | 2025-07-04 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 84b80004-0cc1-353d-a8c2-eb6c2342adbd | -4.0148 | -43.2408 | 2025-07-04 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 20219077-fa8a-32ae-b053-4590ecd52d91 | -3.9961 | -43.2418 | 2025-07-04 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 291fdd86-c8f7-36ad-a474-7bb3bb62f838 | -7.64 | -44.3534 | 2025-07-04 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| b437419e-2535-39bd-9f9a-e10b43f0eb7f | -6.0052 | -44.5189 | 2025-07-04 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 1472f9f5-3eb2-3974-8ffb-3fc1a345a330 | -11.1026 | -47.0217 | 2025-07-04 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 3b534002-eea4-3ad9-ac73-ef94c770d175 | -7.6588 | -44.3515 | 2025-07-04 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 894618b6-c2b2-38a1-a790-10550ce80b5d | -6.0239 | -44.5174 | 2025-07-04 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 566af104-c099-373e-9938-b454b872b749 | -12.6636 | -45.2776 | 2025-07-04 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 460ed198-be51-3829-bace-b8646b08bb3e | -6.6564 | -43.1681 | 2025-07-04 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 82.9 |
| d5e8d4b1-a68f-3bcd-a4fe-27ecabd7e229 | -12.4274 | -50.0171 | 2025-07-04 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 00fb1730-ce6f-33f0-a291-3581ac860063 | -10.2151 | -47.9929 | 2025-07-04 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1de96ae3-3ab3-3e5d-b977-89451bfd4208 | -6.2755 | -43.6907 | 2025-07-04 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8b22a169-3436-3130-ace6-138339c29a78 | -11.1022 | -47.0441 | 2025-07-04 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6cefc6ff-70ea-3b78-a1a6-f9cb32cec037 | -12.427 | -50.0387 | 2025-07-04 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| b501dcb9-c4c1-3f90-b578-c7fac26881c6 | -10.1961 | -47.995 | 2025-07-04 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0d45c89d-96cc-3512-b332-e537fdeadebf | -6.2757 | -43.6675 | 2025-07-04 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |


