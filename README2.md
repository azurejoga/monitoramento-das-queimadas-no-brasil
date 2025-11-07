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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 536fb2d6-71b5-37b7-ba27-85139d4e8bd0 | -10.52112 | -44.60293 | 2025-11-07 00:52:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 79850bea-d092-3e04-8d7c-1a863e3de758 | -14.74409 | -51.60646 | 2025-11-07 00:52:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 268d4b11-3247-3072-ad54-744ab3ec672c | -11.84283 | -56.89666 | 2025-11-07 00:52:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9bfe4ab9-8c8d-3422-843f-07e716b42a5c | -11.73696 | -59.31144 | 2025-11-07 00:52:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a3eef3b9-63db-3265-98fe-b6bdea92c77b | -6.04688 | -57.69497 | 2025-11-07 00:54:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 270f1d80-604b-3d34-b2dd-a5c704df3588 | -4.70755 | -46.43608 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 8394ae5f-5184-3804-a773-327bec903ba3 | -4.44734 | -46.45594 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d7eecdd2-9173-3b42-86f7-90de4417f020 | -4.45357 | -46.46049 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2b47ee12-74a8-3ccc-9261-dcf35b0fcebd | -4.39207 | -46.44433 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.5 |
| a5b1c2c0-9c22-3800-8669-71e81e59c1ea | -4.71744 | -46.4281 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 02e5f804-8ac1-3d8f-9420-4c2566902368 | -4.10943 | -48.02427 | 2025-11-07 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 026ee1e2-eca1-3766-b2e6-079219b8d206 | -4.46311 | -46.45368 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 56151032-a28a-3e42-8a04-2b865bc8a1d2 | -4.72327 | -46.43378 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e10b3853-bd6c-30d1-b535-e7b48fa2a5d2 | -3.53391 | -47.54715 | 2025-11-07 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 59e6e755-1ccf-316c-b9bc-926e54ecd649 | -3.78222 | -45.14145 | 2025-11-07 00:54:00 | TERRA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 18fb7131-d47d-3b1f-8293-31a1960555d7 | -3.59848 | -49.44066 | 2025-11-07 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 532c4a68-e76e-36e9-8b10-c68abb6fd5bc | -6.1214 | -57.71117 | 2025-11-07 00:54:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c0fc4ec7-c0a4-3dee-8205-00cedbe84a0f | -4.40144 | -46.436 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| eec0f6eb-f4e7-38c1-a6c6-0e1a7c0a29d4 | -4.45825 | -46.42277 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 78c2edac-f5d6-30ed-be39-bd940230cae9 | -4.44888 | -46.42937 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 116.8 |
| d7e85ec4-c22e-3bb6-aa4b-991fc79b55cd | 2.20007 | -50.85922 | 2025-11-07 00:54:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 314758e2-1aa7-3f67-8c63-f5547725d11f | -3.78878 | -45.18262 | 2025-11-07 00:54:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a9e61a4d-eccd-32ae-be89-8475ca14b0a5 | -4.44239 | -46.42475 | 2025-11-07 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 40f690b4-e452-36a8-a638-90ffc2a4af52 | -3.78194 | -45.14876 | 2025-11-07 00:54:00 | TERRA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 73bee2f9-caee-3263-beaa-41dda6beb8b6 | -3.53412 | -47.54126 | 2025-11-07 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| d7acb2e9-ee6d-34c1-a714-9402be808f44 | -3.8311 | -52.19567 | 2025-11-07 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 27c8d710-c474-3dde-bd59-aba367f52c0d | 3.09648 | -60.76439 | 2025-11-07 00:56:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| bba503bb-1d3f-36d3-9a18-aa64a2cd1d8f | 2.56141 | -50.98913 | 2025-11-07 00:56:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| be04e1a5-c004-31d1-90c8-0a1d85d02f02 | 3.15134 | -61.02284 | 2025-11-07 00:56:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e8f76638-797a-3989-a529-1954205f824c | 3.1094 | -60.765 | 2025-11-07 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| a52a33f4-0c29-3e9c-99bc-c4dac2c9a6c9 | -5.7591 | -40.7856 | 2025-11-07 01:00:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 46.0 |
| a42b6f35-a8fa-382a-8d84-77db61746458 | -4.46 | -46.4416 | 2025-11-07 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 03f02945-e62c-37dd-8c47-8f5e67fd3b65 | -5.0868 | -44.7887 | 2025-11-07 01:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 6c29ec04-e78c-3e52-bd7e-ae9b111b9362 | -4.4414 | -46.4425 | 2025-11-07 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9e02085d-b602-3b50-a414-5e5ec3ff346f | -2.9435 | -49.3443 | 2025-11-07 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| daf39b2d-0876-3a8c-80b5-024b23e47766 | -4.7206 | -46.4276 | 2025-11-07 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 1c5fafda-0206-3465-aab0-53ab50d1fac8 | -4.4602 | -46.4194 | 2025-11-07 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| fb759ac2-0698-3797-b127-843327fd72b4 | -5.0868 | -44.7887 | 2025-11-07 01:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| cc2c307e-37b1-3954-8075-405fd8bbe857 | -5.778 | -40.784 | 2025-11-07 01:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 1c45dab4-5201-31df-8930-d8bfefd5caf4 | -4.46 | -46.4416 | 2025-11-07 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b36201ab-2e56-3203-922b-2c2443115a05 | -5.7591 | -40.7856 | 2025-11-07 01:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 7958742e-54d2-3c2d-a951-8bd36500057d | -5.7589 | -40.81 | 2025-11-07 01:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 80bcc78e-b190-3573-95b3-8f50aab01972 | -5.7777 | -40.8084 | 2025-11-07 01:10:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 48c40b11-7194-3bc4-b301-15012e95ea4a | -4.4602 | -46.4194 | 2025-11-07 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7a1b7dba-b3f3-3db2-bda0-be1542c56e37 | 3.0911 | -60.7653 | 2025-11-07 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 50f4e685-7344-33dd-b38e-a0222aea5cf5 | -5.0866 | -44.8115 | 2025-11-07 01:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7df70802-0fa3-3adf-9b82-51351b2e115c | -4.2962 | -45.8715 | 2025-11-07 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8c90b300-791c-3393-94ac-9f1d9f29ff6e | -5.778 | -40.784 | 2025-11-07 01:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 5b37923c-db24-30ad-907f-91cda02a9005 | -5.1535 | -41.2226 | 2025-11-07 01:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 1a8e1f2d-7da2-3648-a142-49dac3a0f6de | -4.2775 | -45.8948 | 2025-11-07 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 03eb63e7-f8b8-38da-a1b5-db8f6619f0b2 | -5.7591 | -40.7856 | 2025-11-07 01:20:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 63.3 |
| 67783d33-9fc1-34b1-a6f7-648f1a2864dc | -5.1723 | -41.2212 | 2025-11-07 01:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 64e783a5-cad2-3d58-91ca-add67f6188e3 | -4.2961 | -45.8938 | 2025-11-07 01:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 104.0 |
| d729f557-450a-3e90-bf37-8428299da2ae | -4.46 | -46.4416 | 2025-11-07 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3ee50a9d-0103-3741-8668-51464d0402a5 | 3.0911 | -60.7653 | 2025-11-07 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d709a308-85cd-33a0-a06e-610e6fcc1eb9 | -4.2962 | -45.8715 | 2025-11-07 01:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 29c26240-4a2c-3cdd-a7cf-027576cf1a6b | -5.0866 | -44.8115 | 2025-11-07 01:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d14df072-cbd0-3b77-b0f2-004d4b68d22b | -4.46 | -46.4416 | 2025-11-07 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| b658838e-43bf-35c9-870d-4f57504a4852 | -5.778 | -40.784 | 2025-11-07 01:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 8cbb79f2-adc4-392a-8c71-e61230bc3312 | -4.2961 | -45.8938 | 2025-11-07 01:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 1187fb3d-3a85-3660-b947-76177350f11c | -4.2775 | -45.8948 | 2025-11-07 01:30:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 8c46716f-8e58-38b9-bff1-4b025ab66440 | -5.0868 | -44.7887 | 2025-11-07 01:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| f6cc2ec4-80e6-3209-bf87-c459c3966889 | -5.7591 | -40.7856 | 2025-11-07 01:30:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 32019c0d-0c75-32fb-803e-ae10babf90b0 | -5.1054 | -44.7875 | 2025-11-07 01:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4f819fc1-da84-33af-b1d0-6abb5061db5f | -4.2961 | -45.8938 | 2025-11-07 01:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 7cce4a0f-6943-3086-893c-e20bc6bd9d11 | -5.2737 | -47.168 | 2025-11-07 01:40:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 726fc77a-5f0a-3307-9bb0-31d9f9fcbd68 | -5.0868 | -44.7887 | 2025-11-07 01:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 41da71e1-6d3c-35fc-9f13-8f1be54f5d89 | -4.2962 | -45.8715 | 2025-11-07 01:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c1d60bfb-5e96-3364-bb73-0d5b7ef893a6 | -4.46 | -46.4416 | 2025-11-07 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ea13df49-caf5-314d-aa58-2bc01b84a5b6 | -5.0866 | -44.8115 | 2025-11-07 01:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1bc00b09-b0e5-30f5-9d07-d4c5e4c227f6 | -4.2775 | -45.8948 | 2025-11-07 01:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d63d2bb8-6e33-3a59-9850-1c67f5820599 | -5.1054 | -44.7875 | 2025-11-07 01:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| e7cb18a4-1b98-322b-9e86-293acb0f6e01 | -5.0866 | -44.8115 | 2025-11-07 01:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 39091d1d-ff6c-3b71-9b57-759c2325ee11 | -5.2737 | -47.168 | 2025-11-07 01:50:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c27de4dd-04e6-391a-8e79-74deea4ac960 | -5.1053 | -44.8103 | 2025-11-07 01:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e28390ac-fd46-3389-866b-eec0a512ac85 | -5.0868 | -44.7887 | 2025-11-07 01:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 2f8c1ffa-c8e7-38cd-8854-1b8cb6e8fede | -4.2962 | -45.8715 | 2025-11-07 01:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 308f0955-0f49-3210-8938-a5a5d4d6aa71 | -9.4349 | -59.2154 | 2025-11-07 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 531896e0-50d7-3f71-b769-8206eb80a2b4 | -4.46 | -46.4416 | 2025-11-07 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 93812236-a911-332f-9830-1a0dee316931 | -9.435 | -59.1959 | 2025-11-07 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 15c7f2ab-b300-3f85-a4bb-2c54c58f7794 | -5.7591 | -40.7856 | 2025-11-07 01:50:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 96525c50-cf72-39e4-904c-554198a79145 | -4.2961 | -45.8938 | 2025-11-07 01:50:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 43e3b977-4192-3ee2-8f19-2ce84162e7a3 | -5.2737 | -47.168 | 2025-11-07 02:00:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c1d13316-9b81-3f96-8768-091674d5040d | -5.0868 | -44.7887 | 2025-11-07 02:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 59bd6b27-6c66-340a-bfbb-a45c89cacbca | -4.2961 | -45.8938 | 2025-11-07 02:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 5e60dd04-823c-398a-95f9-abba1ab142cf | -4.46 | -46.4416 | 2025-11-07 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6b8351b2-7f62-3d74-9b99-019287ec9540 | -9.4535 | -59.2143 | 2025-11-07 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c939fe69-aab3-316f-9106-b98c63262969 | -5.778 | -40.784 | 2025-11-07 02:00:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 57.4 |
| d54e63b5-ce88-3c59-acc1-2de4d520ee31 | -5.0866 | -44.8115 | 2025-11-07 02:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 1f7c4df4-eb7f-338b-8d9a-c35564e647b4 | -9.4537 | -59.1949 | 2025-11-07 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 5ac9ed33-bf0a-3d9b-89a8-c8570fec8b04 | -5.0868 | -44.7887 | 2025-11-07 02:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 3c3112aa-745a-3b62-b879-63db9537d33e | -5.1054 | -44.7875 | 2025-11-07 02:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 251d4f05-aa33-388d-a164-2361b1f551cd | -4.2961 | -45.8938 | 2025-11-07 02:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 292c9d99-e0d7-3905-9e30-02137ac0d6b2 | -4.2775 | -45.8948 | 2025-11-07 02:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 45f7bb53-e669-3735-923e-56aa5c5b18fd | -5.0866 | -44.8115 | 2025-11-07 02:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c2dcf981-7061-3602-9e87-c9de33cf95ad | -4.2961 | -45.8938 | 2025-11-07 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8e795596-1fb2-3a79-92dd-78a998af602f | -5.0868 | -44.7887 | 2025-11-07 02:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| ae50c82e-2d59-3be4-875b-d1bcae4fbf3d | -9.4349 | -59.2154 | 2025-11-07 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8d509506-35a2-33a5-a9db-232d669d9e27 | -5.1054 | -44.7875 | 2025-11-07 02:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 4ad1e5e3-bc93-371c-bb40-de03bef5aea3 | -4.2962 | -45.8715 | 2025-11-07 02:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 43.1 |


[Clique aqui para ver as próximas entradas](README3.md)
