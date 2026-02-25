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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94ac8fab-dce5-3a10-8ed5-534cada3fe03 | 1.4864 | -59.9308 | 2026-02-25 11:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 816.8 |
| f71f4abf-bd68-3363-9399-6ce3c7d658a0 | -8.65308 | -35.98999 | 2026-02-25 11:32:00 | TERRA_M-M | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ad0af72d-e2bc-3a4d-9495-b6f9c9d55330 | -9.105 | -36.73755 | 2026-02-25 11:32:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 226db457-943f-3ca5-8cee-41fa73f74713 | -8.51963 | -36.65759 | 2026-02-25 11:32:00 | TERRA_M-M | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 66009231-7a3c-3a4a-aa9c-aad902eab322 | -9.2625 | -36.79107 | 2026-02-25 11:32:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| eb600711-1984-3b48-ba04-fe281f07d0f8 | 1.4681 | -59.95 | 2026-02-25 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 212.4 |
| 47f0adc8-717b-384e-8e28-b44cd3e5fe95 | 1.5046 | -59.9497 | 2026-02-25 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 4ea64353-6a2c-3df8-85dd-95b320b61cfd | 1.4864 | -59.9308 | 2026-02-25 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 611.9 |
| 01cd5d10-88f8-3e0c-815a-c293f7da9bfd | 1.4864 | -59.9498 | 2026-02-25 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 863.2 |
| 0911ba39-da3e-3834-9abc-d592bfb19086 | 1.4863 | -59.9688 | 2026-02-25 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.6 |
| c2298799-636d-3a15-9c8c-a931a8f4af36 | 1.4681 | -59.9309 | 2026-02-25 11:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 92583225-0239-3038-b6ee-0499756dd79b | 1.4681 | -59.9309 | 2026-02-25 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 199.1 |
| 39da3e68-350d-392e-936a-5ee9e0c52ca2 | 1.5046 | -59.9497 | 2026-02-25 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 84248608-98bd-3465-90b0-f5ea1b5c6088 | 1.4864 | -59.9498 | 2026-02-25 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1023.4 |
| 0d0309ea-1943-3430-bc09-17fe2ad840e1 | 1.4863 | -59.9688 | 2026-02-25 11:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| d5926c3e-ea0e-3f4e-9e52-fa2e4800f486 | 1.4864 | -59.9498 | 2026-02-25 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 974.7 |
| 92bafc0e-ebd3-3824-ac34-7136480f1559 | 1.4864 | -59.9308 | 2026-02-25 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 603.6 |
| 62c51071-954a-3f75-837f-99d5cf654607 | 1.4863 | -59.9688 | 2026-02-25 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 175.5 |
| f967ffba-158a-3ac6-974a-2ba7ac800f5c | 1.4681 | -59.9309 | 2026-02-25 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 170.7 |
| 4323f57f-ade9-3c3b-9818-d9fb1d9b2757 | 1.5046 | -59.9497 | 2026-02-25 12:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 2230fdd4-cb2d-36f7-bee9-b54f7de9c206 | 1.4863 | -59.9688 | 2026-02-25 12:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 467dee10-512f-3863-a66c-32b779b07eb8 | 1.5046 | -59.9497 | 2026-02-25 12:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.4 |


