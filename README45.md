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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3128f790-92e3-38ba-8502-83fbd84bd86d | -3.17109 | -50.39069 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b5884bf-babe-3673-8097-3c415ee6cb4a | -3.1677 | -50.39017 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1a6a305-693f-3d68-990e-e49f08e08f47 | -3.16489 | -50.38601 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf2a438e-9587-35db-8edf-723fd0b4d9a8 | -3.16431 | -50.38964 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e8369d-2a76-3317-ba33-5fd14e272768 | -3.15267 | -50.46263 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5443dfd0-16a8-3b06-8bc5-4fd6dcb2c0bb | -3.14986 | -50.45844 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6575f610-e25e-3f5b-8e9b-157783c65073 | -3.14704 | -50.45425 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18f3cec5-f377-3338-9f59-0bb290143163 | -3.12526 | -50.36514 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e0e1bad-dfb5-3b05-b861-02f4f60d4058 | -3.12473 | -50.34642 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63f0f647-ca5e-318b-af6c-c3a3f2ce7216 | -3.12416 | -50.35006 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7c47711-1b93-3c58-9b8a-a6cf81bf705f | -3.12187 | -50.36461 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1bee149-1729-30cb-b040-4f5d29db8023 | -3.1213 | -50.36823 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee58b92f-9a38-3be0-83b4-8d3355d33599 | -3.12077 | -50.34954 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a850539-d5e6-3c9a-b4d1-536033cd1053 | -3.12019 | -50.35318 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37efeed4-66c5-3da2-8d41-87eb59c8386b | -3.11795 | -50.34536 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af4e4cd1-3221-3609-bc92-f03b5ee08910 | -3.11738 | -50.349 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e5d7201-cf04-3940-8a46-4ea3110de071 | -3.11681 | -50.35264 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5846e4f-79ff-300e-ad67-2827be3fc0c3 | -2.29434 | -49.26518 | 2024-10-29 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 11d10309-3b57-3fbf-b7e4-58a54b7f1273 | -2.23818 | -50.31347 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d98afdcd-0c8f-3d4a-8cf2-9cc6bc834a3a | -2.482 | -50.28004 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67314e98-acc8-3c6f-950a-8d810c19e7a1 | -2.47803 | -50.28316 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a29d7a92-b1be-3915-a2f7-74c33ed4ef64 | -2.47406 | -50.28629 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e04aaf09-adbd-3421-8d8e-42fefc89b61e | -2.47009 | -50.28941 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cb5e9e7-013d-3999-bdc8-aaa87269b5c9 | -2.46069 | -50.41584 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 432298cf-e857-3b7b-b56c-b53f96608d66 | -2.45728 | -50.4153 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 982dbedf-d54b-3a38-afe6-4cd5e81800f5 | -2.44943 | -50.37635 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a7bddab-bdb0-3a31-9572-76a162e4914e | -2.4293 | -50.28313 | 2024-10-29 04:38:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d146020c-aa1e-3ff1-be5a-fe11840bf066 | -2.41457 | -50.42004 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba16d52-ac0a-3d3d-97cd-e4842a436c1a | -2.41115 | -50.4195 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1f4ccd2-f035-3259-81bc-c8ceb922a256 | -2.40998 | -50.42689 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b20a50c-2030-38c9-a500-456bbeab077d | -2.40774 | -50.41898 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab1e9328-8571-3595-a8ad-8d836fd7e3cd | -2.40715 | -50.42266 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57fa612-ddc0-3dee-b57c-4e24d9598d1f | -2.40432 | -50.41844 | 2024-10-29 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30de399b-c68f-36f4-8078-daa18108f0b9 | -3.52658 | -49.24029 | 2024-10-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92229d67-83d9-3549-b346-4c1d6e17c0ba | -3.52604 | -49.24374 | 2024-10-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43da5e71-7a75-35e0-b71a-12e58c0ff928 | -3.15499 | -49.18147 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09ecb930-7a57-32eb-b522-9339c8550a17 | -3.14176 | -49.17942 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86188596-8fe9-3ef1-aebe-52156ec777c4 | -3.13846 | -49.17891 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63dd70c1-03bd-3071-a47a-9cd03f0fba80 | -3.13293 | -49.17098 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f4a2c211-2575-3733-b0a9-c8291eaec73c | -3.13239 | -49.17443 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8b8ca3f-919e-31a4-be5f-9a9cee271fe6 | -3.12324 | -49.29681 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99627a4c-e386-3d62-bd1d-312454360a5d | -3.11993 | -49.2963 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c06de03-18ce-3dc1-8b53-cbe4ff629138 | -3.08848 | -49.21304 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6131712-0e1a-3226-bdff-3768d55e499f | -2.96054 | -49.09765 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96b323ea-4ae0-35a3-a008-88af16804ecb | -2.95201 | -49.21647 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aca9573f-8af2-3797-aced-e65a9a206b21 | -2.85267 | -49.1338 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c9f1a8-8c48-37b2-b9cf-8a895adc73cc | -2.84249 | -49.26315 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38e0aa24-350b-3a23-8c28-3f1626e5344f | -2.83918 | -49.26264 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfcc8482-b88b-3cfc-9c50-648549614879 | -2.83636 | -49.23739 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6000049-821b-3cce-9191-34f9f39ecbcb | -2.83586 | -49.26212 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa12b665-01bd-312f-b3f1-7734173ab91a | -2.83582 | -49.24085 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef56f34b-26ff-3bfa-a6f9-160f5a8ca1cd | -2.83527 | -49.24431 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c927d95-09a1-39c8-b8d8-5505e2889b63 | -2.83251 | -49.24034 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 927ebe43-3ac3-3931-aa81-86a445e9afab | -2.83196 | -49.2438 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1043ed90-90de-3e9a-9d86-8bf8bb1aea8e | -2.83029 | -49.23291 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 9600aeae-b57d-33af-9079-5b0749c83d9e | -2.8292 | -49.23982 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6701513d-580f-37f2-82ae-18a1faf8666d | -2.82697 | -49.23239 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 0e8c3564-d709-3e20-8363-ff9a6f050c47 | -2.82534 | -49.24277 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c25e422-9023-3663-8b63-1bf7e87a5a37 | -2.82366 | -49.23188 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a8e92288-25fc-3f48-8ec6-7ad7346d240f | -2.82257 | -49.2388 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95b701f5-0f09-3b69-bb55-effd9fbc42e7 | -2.82094 | -49.24917 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf235ef0-8dbf-30be-ae63-10b29da98807 | -2.82035 | -49.23137 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5acb756e-c8d5-34c4-8fe3-0d9eb73eb12a | -2.81981 | -49.23483 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f42eee2-2dbb-3195-a401-ee09982b5617 | -2.81872 | -49.24174 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9a40a9b-1df4-3eb7-93f4-b0ccfbc8cf5d | -2.81758 | -49.22739 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9ce05e4-9a78-32f8-95e6-4775d39de77f | -2.81536 | -49.21997 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d5dfe037-7413-3474-b983-8448fa4bb367 | -2.81482 | -49.22342 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f4be921-67df-36a1-9f3c-df751e344b9b | -2.81427 | -49.22688 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6299947-f89d-3157-8bc2-8f9652a4c666 | -2.81205 | -49.21945 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dff50381-1975-3d85-b49c-daf033e1282c | -2.81151 | -49.22291 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef4c18ad-db55-3013-9560-9e678b27b215 | -2.81096 | -49.22636 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5198195-ebdc-3784-9a23-9052a51710c7 | -2.80874 | -49.21894 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 887a38ce-87f1-324e-ad99-54851b4c08b6 | -2.8082 | -49.2224 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 61873a1d-d4f9-30d3-9921-2d054902c54f | -2.79441 | -49.2238 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 236671a1-8d1c-3975-9e78-836daa79c7be | -2.79386 | -49.22725 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ed35498-2f8c-3507-9351-708ba676767c | -2.7128 | -49.05126 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5d94ee3-7a7e-39e8-9e9d-fef37d43b98f | -2.71226 | -49.05471 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93251421-05b0-3b69-879b-afdac2f33a96 | -2.71172 | -49.05815 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64ce7275-aa0e-3880-8d0b-d4a155abccb1 | -2.71004 | -49.04731 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 704faae2-e02b-321b-8743-22e9363474b8 | -2.70895 | -49.0542 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e482fec-592a-32eb-b9ab-60c61cb8d525 | -2.70841 | -49.05764 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbca0763-946f-3b6f-a087-d9320ab1012d | -2.70565 | -49.05368 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85df24f8-8d5f-32da-8b65-65b70ba06781 | -2.70511 | -49.05713 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c75a4a24-9158-34c3-b671-1b3675216013 | -2.70343 | -49.04628 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a31086d5-7f15-3e1b-899d-08012260ec21 | -2.70289 | -49.04972 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ba11e4b-df68-3cff-831d-3cf451d184f4 | -2.70234 | -49.05317 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9c778a8-d04d-3db4-a2b2-a2922d6646a5 | -2.7018 | -49.05661 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dca5213-b431-35b5-bdf0-b2d0158c9caf | -2.69904 | -49.05266 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3360c172-a96c-3e64-8141-db23bcb30735 | -2.7095 | -49.05075 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e46afb1d-3bad-35af-bd9c-86f6762b54e3 | -2.70619 | -49.05024 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfed4162-138f-364e-9acb-b1c2432862e9 | -2.66465 | -48.98733 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14fa118f-4bce-3619-96f1-a9201e0f5f30 | -2.57329 | -48.96243 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7a4087d-2de0-3e00-a530-4ad55fc2baea | -3.09233 | -49.2101 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad6431e6-7c0b-3a14-98f5-5fb10112adb5 | -3.09179 | -49.21355 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a461eab2-d1e0-3d71-9179-91a95e168ca5 | -3.08902 | -49.20958 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| baa2428d-0810-318c-8429-3d75394eb67f | -3.08793 | -49.30551 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf738779-a1b0-3696-811d-7eeff70c477a | -3.08154 | -49.30046 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c2bb2de-8e4c-3970-9ec9-8a9a568014b1 | -3.0804 | -49.52481 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 942ca7c7-51f2-3728-bb87-d19f53a1764c | -3.07985 | -49.52829 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15dc95b2-34e9-3c03-84da-7b6828e89600 | -3.07598 | -49.53126 | 2024-10-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README46.md)
