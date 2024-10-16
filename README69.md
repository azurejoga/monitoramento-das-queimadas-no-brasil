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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9482aec-07fc-35b0-8174-92e17af8f22e | -15.91717 | -56.31236 | 2024-10-16 05:50:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c73f9768-b74d-3717-8ef8-c3ac619b83f8 | -15.91658 | -56.31819 | 2024-10-16 05:50:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1922d61b-ce6a-3aed-9607-c3c22443b8af | -19.60063 | -56.95296 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b8714c92-7af9-37a2-8bb3-358e84f2b688 | -19.59861 | -56.97633 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 5510f11c-9f1d-3c42-84be-0365bc0907f4 | -19.59811 | -56.98215 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.0 |
| b1ab7864-7c6d-3cfe-a42c-689ebc5e6ce0 | -19.5976 | -56.98797 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 31df7e93-9e82-3155-82ab-60619af60fa7 | -19.5971 | -56.9938 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 25dc6abc-a04e-3d44-9deb-06fd7c23569d | -19.59454 | -56.94645 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4df116f0-c324-3fc8-b698-bc4c5a4c93b1 | -19.59404 | -56.9523 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 07472e51-f772-3fc0-90ea-2126d1425226 | -19.59353 | -56.95816 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4eb630e5-0138-3fcf-84bf-5dbcd60fa389 | -19.59253 | -56.96983 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 1164160c-b4db-32d0-bca5-474730d8a563 | -19.59203 | -56.97566 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 55b11820-01a7-398b-a1d3-3ee2c664797e | -19.59153 | -56.98148 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.4 |
| dd81e11d-5e66-329c-993c-17af3874ea78 | -19.59103 | -56.98731 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 9f88f523-6326-3ee0-af72-434c73b0b288 | -19.58745 | -56.95164 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e5a102e5-b04e-36d9-834b-f42875e4fca8 | -19.58694 | -56.95749 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a31f86fb-ea24-3dff-9a6c-a16f6a2f35fa | -19.58644 | -56.96332 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2ebee0c3-bd21-37a6-909c-b281843ac305 | -19.57986 | -56.96265 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4d41174d-cdf0-3781-91b0-e37f9f32136b | -19.57936 | -56.9685 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bb9c1763-df40-3d21-a0e1-547252fef24f | -19.57886 | -56.97433 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 97291fb3-d5e3-3924-aca5-004ea374e858 | -19.57837 | -56.98016 | 2024-10-16 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| bb05214c-0599-364c-b68a-f0032ab9d792 | -15.16475 | -59.71672 | 2024-10-16 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cbc724b-0e76-37e3-9a4d-8231fab53442 | -15.16444 | -59.71618 | 2024-10-16 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cc6fe45-36bc-3fe9-a845-5f0f3562004f | -15.16436 | -59.71999 | 2024-10-16 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c217025-05e4-3db9-8afd-ce3e3cc2aa19 | -15.16407 | -59.71946 | 2024-10-16 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebdb3a5d-846d-32d3-9554-2815a7c95f54 | -15.16396 | -59.72325 | 2024-10-16 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ff0cac1-473c-3573-80e4-f6f8fdca9dd3 | -15.1637 | -59.72274 | 2024-10-16 05:50:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7681bf9b-7797-31ae-9d94-0654ca98fd9d | -12.11695 | -63.76225 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c33bcba5-e729-30f6-b39f-465ef0a61068 | -12.00435 | -63.51275 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7753972-b112-3dc7-a5dd-5238897e9952 | -12.00367 | -63.51773 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b2e790-4bf5-3744-a62c-b511798dd018 | -12.00117 | -63.51072 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02ba6617-4d2f-35a0-b6d6-1a49e3f22036 | -12.00045 | -63.5157 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85cb0417-c5ee-3499-b4ed-f36f36c4123f | -12.00045 | -63.51215 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b51a11ee-336f-3226-9e51-bc12efbe3bb8 | -11.99976 | -63.51714 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 023f779f-b6b9-378f-bc66-28ca3a65333e | -11.99654 | -63.51157 | 2024-10-16 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f17a8df9-eb2b-3d7c-b48e-49f21e6e39af | -11.79732 | -64.17217 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b2f79e-19e0-3e60-85fb-3b85f0320205 | -11.79711 | -64.16911 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72a25d6e-446f-3b07-b54b-44becdac6cb6 | -11.79485 | -64.16249 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8361c4fd-2a98-30cf-8e73-cd8dfd5108df | -11.79403 | -64.16401 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69de8d0d-7b1d-3717-8e6d-f0e1cd17f90e | -11.77022 | -64.09014 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9ef7075-2425-309f-8e00-0bbdf3e64d87 | -11.76712 | -64.08498 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b80a4137-1ea6-39a6-84e5-99b0d536428d | -11.76645 | -64.08961 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a90f7714-5f33-384a-9970-1d3f2d691ab5 | -11.75912 | -64.06027 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b82dec0a-b79f-3eff-8f8f-bfd4eb474a36 | -11.73467 | -64.04254 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a694500e-2f88-30ef-b168-f3e4bd379784 | -11.73402 | -64.04716 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f5c68de-36ec-3384-9200-91eea083c29c | -11.73336 | -64.05174 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d228bc-4cb7-3c98-bf97-9dad4f395500 | -11.73023 | -64.04665 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a5cccb1-ce84-35bc-873d-ae4f6259fb71 | -11.72594 | -64.02247 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4204a6ce-7b76-388c-8775-ffab7c34cf30 | -11.72215 | -64.02199 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1a2dd57d-6edc-3991-aed5-6958427e3157 | -11.67771 | -63.93265 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fbe6d14-a6e3-3de1-a4c4-1136a781f3f6 | -11.66862 | -64.26573 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e0618d0-a969-351f-a5a5-be7a10ad1010 | -11.66799 | -64.26344 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46c540ef-3f60-34b2-a244-c4738e69404c | -11.66561 | -63.93592 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 758a9d8d-61f5-3043-af05-97e132de69d3 | -11.66489 | -64.26517 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42deafc8-87e6-3dca-b891-946520fec635 | -11.66427 | -64.26289 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38010e28-c20d-3543-842b-ad3e456a4079 | -12.13715 | -64.73672 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 160f456a-2a59-3283-a89b-f13faf513756 | -12.13349 | -64.73618 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d6bbf7-5ebf-36ba-9160-ca67610f0c8e | -12.05991 | -64.67667 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b27b6fc-afaa-3bb1-a92a-47307feca811 | -12.05625 | -64.67612 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd10f3ff-0ca1-3712-bf1b-3e1b9d66c99b | -12.05563 | -64.68046 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a696fd5a-9723-32c2-8ace-b899858f3888 | -12.02056 | -64.72137 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 696cb04a-8098-3da0-99e5-b1af15f4673a | -11.97789 | -64.73258 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0f42bd6-1118-3574-bf4c-e90597ffd720 | -11.96322 | -64.75668 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4b60aaa-81f6-3d97-8a57-36b6c464948b | -11.96175 | -64.84359 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8434a8e6-030a-3884-939a-8fb2dcf05b63 | -11.95896 | -64.76044 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a01eb3b-09a9-3b76-b217-3f249a4358d3 | -11.9547 | -64.76418 | 2024-10-16 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25d583a9-8931-3703-9563-6b0e05b89885 | -12.39413 | -63.71639 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17807cfe-2ec0-3b89-9452-7fc0d8a5dbb8 | -12.39402 | -63.71899 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 191c8912-94d1-3a61-8dac-95279cb8cde9 | -12.39132 | -63.73865 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73efd4ec-79e0-30a2-a779-725ffb3cd2d9 | -12.39095 | -63.7109 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6492b51c-9245-3d87-a0e5-215d234a6227 | -12.39081 | -63.71348 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2682fc22-ab92-33f3-b3a7-eefc5b725f22 | -12.39024 | -63.71583 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e3fb484-c36a-35aa-9be8-f1affda3491d | -12.39014 | -63.71843 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 343b7eb9-c6c7-395a-8188-afdc3b6e7cde | -12.38953 | -63.72076 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 904e1720-4801-3452-8a85-3b5489cb490a | -12.38883 | -63.72567 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1991f90b-8a3e-3dc1-b68c-aadb0950f4b9 | -12.38778 | -63.70541 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c6ecc70-f989-37c9-89b9-9dc7fcf5cb91 | -12.38761 | -63.70798 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d2bfb707-2edc-3180-9f2f-47b213b80074 | -12.38707 | -63.71034 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 091f8a45-0abc-3c42-af31-3595d2dcec83 | -12.38693 | -63.71292 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f51f5236-c02a-3afe-ac9d-99345f420c63 | -12.38636 | -63.71527 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a5c32d5-f9dd-3732-8a27-e00236525e68 | -12.38625 | -63.71786 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0bf6db3-e4f7-3c60-adbc-8582bdd37500 | -12.38558 | -63.72279 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1821ced-a529-3bef-a3f3-860360a97147 | -12.38495 | -63.72511 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ad61b6c-3da2-3eac-b758-218fdcec401b | -12.38491 | -63.7277 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2a1285d-2e4d-3beb-a2a5-97195d71c211 | -12.51008 | -63.97073 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9336bf09-deee-3229-8f0b-58111268d381 | -12.50624 | -63.97017 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfd691f7-afca-39f6-b665-84f18e344035 | -12.50261 | -63.9403 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28c71fdd-d528-3ffa-b36f-35b840867751 | -12.49427 | -63.94397 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb887efb-83e2-30e1-aa6b-a03503b44d1b | -12.49408 | -63.97329 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d43beae1-2e7c-394e-a7ff-03a647f0223d | -12.49025 | -63.97273 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fd43e1f-3def-3337-9aed-83c9be4ce3ab | -12.48709 | -63.96739 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e963e2f7-3c4d-38e8-a8b7-0f6c42566ae0 | -12.48674 | -64.0257 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2da11d8c-1a36-392e-8f5e-cdecad41259f | -12.48607 | -64.03044 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28556452-b68a-3942-8f5a-687665a36913 | -12.48526 | -63.95245 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d974d40-fc6f-3c2e-aae6-ed437380a109 | -12.48459 | -63.95724 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1af52de4-00c8-38dd-a6b9-3282b36bc682 | -12.48326 | -63.96682 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54b5f57c-0b72-3508-8175-bb57e1b3e21c | -12.48292 | -64.02514 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c81faf30-3568-33b4-b961-0c22f99455bc | -12.48226 | -64.02989 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdeabde9-dbe7-3aa5-8d49-2c742fd17344 | -12.48076 | -63.95668 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d3dc717-07c1-3b28-b70b-0ebfd74d219b | -12.48043 | -64.01508 | 2024-10-16 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README70.md)
