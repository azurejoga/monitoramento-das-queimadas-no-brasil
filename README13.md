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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66abc8a7-37eb-3629-8e94-091f856721d6 | -12.60308 | -57.88424 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 894621a6-1707-3b95-be88-c34c74cd06d3 | -13.24343 | -54.40906 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6bf7c59f-94e8-359e-8016-da4886c530b7 | -13.8343 | -47.14434 | 2026-06-27 04:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d62dc23b-1227-306a-acd5-727a4d007cda | -10.12322 | -52.10699 | 2026-06-27 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce2d3341-3764-352a-8012-92b00ab1a146 | -14.61018 | -48.00528 | 2026-06-27 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87135511-b89a-349c-858b-a23f2f7a6610 | -9.95751 | -51.09798 | 2026-06-27 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0689ef99-b321-369c-ad86-485872dafedb | -11.64484 | -54.893 | 2026-06-27 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ef7862a-e02f-3415-b30b-fcfe871dc70b | -8.78512 | -46.92629 | 2026-06-27 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ab9e960-22af-343e-81ad-dc54abb0df38 | -10.47583 | -47.08393 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0add468c-7faa-340d-b244-84ee2b7009e9 | -9.53318 | -47.75559 | 2026-06-27 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c943216-6c9a-3ce2-9c75-6e7ce2cb9dce | -13.64858 | -55.29555 | 2026-06-27 04:32:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94a36598-0556-3bc9-9985-3f292787d07a | -8.99072 | -47.74678 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b371f42-b944-36d0-bb10-f2a3180cb662 | -9.88132 | -52.44406 | 2026-06-27 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d30280b1-abf8-37b8-9904-c22e8049c56d | -10.49844 | -47.13411 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b72337b-408a-3e7a-8d29-1cbff1ffd582 | -11.91911 | -44.99777 | 2026-06-27 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae1c2e28-e4d0-31b8-92c1-ad38dd8f7d43 | -10.62815 | -50.21709 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06028d3b-bd01-30d2-b680-9d36b54dc0e4 | -10.72086 | -56.2289 | 2026-06-27 04:32:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f01c0c37-277a-395e-98ed-f08c3e068918 | -13.22699 | -54.42418 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81ed1c0e-8262-3fad-817e-68f9c5d81b5d | -10.80665 | -55.86176 | 2026-06-27 04:32:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a86d9659-aa10-344c-a4fa-6f1ca86a599a | -11.90439 | -57.41282 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f60f4caf-6513-35df-89c8-b9540e423d29 | -10.47364 | -47.11937 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f6cb22da-a3e4-3e3e-b02e-273acbda744a | -12.46245 | -58.49883 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e9cce196-38f3-3ddf-af6a-710b9fe9fd62 | -12.07974 | -54.61049 | 2026-06-27 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a151a7b-38d8-3266-8246-f7b492301d4d | -10.47309 | -47.12286 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85baed9b-3716-3421-8389-c0fccf903a25 | -11.91604 | -57.41129 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f615a521-46c2-3a3f-8ad9-b1016c7d76da | -10.68938 | -50.24446 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b4670e2-ce07-3f56-bd1f-b213bc885c99 | -9.13958 | -45.28166 | 2026-06-27 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb50b4c6-9763-3a9f-8620-d51411280163 | -14.61073 | -48.00172 | 2026-06-27 04:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 614a5e91-e586-3ddc-b670-5874c68704bf | -9.69303 | -47.69093 | 2026-06-27 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 853d700e-4c59-3559-898d-67774228956f | -10.55551 | -46.24847 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72ae2d03-beb1-36ee-be72-7791523642e2 | -8.59063 | -46.90967 | 2026-06-27 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19fd3876-3caf-3e26-9d63-fef480d22116 | -13.88146 | -47.17059 | 2026-06-27 04:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9fbfa370-c428-3774-b2a5-e5c68ae5f545 | -12.55104 | -54.5862 | 2026-06-27 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5b220f2-21a4-3bae-9820-48dcabe8bfbd | -10.55271 | -46.24442 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d6e172f-fd9a-338d-8a7a-155f9eb1ed67 | -12.51523 | -48.27659 | 2026-06-27 04:32:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e7a1a51-8ca8-3522-9b09-7211b0cf169d | -10.78864 | -56.75628 | 2026-06-27 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4b5150b-34cb-34d7-8ffb-3e8e6f188b8b | -10.9328 | -56.85925 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ba84902-eca0-330a-9909-2da6c437ee0c | -11.90947 | -57.41326 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5284382-4066-3996-8b71-c45920297f76 | -14.87803 | -54.54403 | 2026-06-27 04:32:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 464965a9-d00b-3aef-a67a-74cbc33d70d5 | -12.61269 | -57.89411 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3ec1f7e5-f33a-3cd8-8693-5b4f94efc9f4 | -12.93593 | -56.63565 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51b526ad-2076-3656-8234-d719419c8d0d | -10.48136 | -47.13494 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b25ab2d-8017-3d5c-9bad-88911f9869fe | -12.45667 | -58.49761 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e0b09041-2835-3c9e-936a-5bb77b976024 | -11.91563 | -57.41069 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a27d899e-985f-3374-b2e9-f8491b1c46ee | -10.50891 | -47.11073 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76820916-40d3-37ea-9b9e-d6c2c7b2edc9 | -10.53926 | -53.71527 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac9b583b-c3ee-3db5-9fb3-5b92d9426508 | -13.83873 | -47.13777 | 2026-06-27 04:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef80756a-aeb0-37e2-93c4-d44b7268c902 | -11.91493 | -57.41438 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a67ef97-95e5-3144-881e-6c45fc54a2d1 | -10.47804 | -47.09146 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d16691d-428f-3051-8ee1-9f4937ad1ba4 | -11.79111 | -57.34877 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abf0e452-2a81-3da8-90e3-1491a0dbc153 | -12.62378 | -57.8965 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 79620f44-d9cc-323e-a8a7-f2bf9b10ddf8 | -10.38482 | -56.72153 | 2026-06-27 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 925e649c-5096-3af9-b507-38656bac5aec | -9.07219 | -44.76291 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d41a9123-77dc-3fb0-9ebf-0491331fb686 | -14.87453 | -54.53899 | 2026-06-27 04:32:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f807822c-9807-31cb-8fa6-5957ce23efef | -11.31009 | -51.39206 | 2026-06-27 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bccf22d4-19e2-304a-aa90-c1f22ffaeeff | -13.66569 | -53.94207 | 2026-06-27 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be227d5d-53bc-3143-9e2c-31d646e92fdf | -12.9347 | -56.64194 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 137d68e6-6c87-36d1-9677-7c61b2240994 | -11.91838 | -57.10263 | 2026-06-27 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b033da8-9d58-363d-b961-83938003d1a0 | -10.89943 | -56.85922 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61aa26d2-56bc-33ea-8600-3084e2ea19a1 | -9.424 | -50.67858 | 2026-06-27 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0257e45-b0d3-3c2f-8c86-a45e3103600b | -9.0716 | -44.76671 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d7f8545-dc8e-3f94-9669-a964e5dcd70a | -12.17172 | -59.75375 | 2026-06-27 04:32:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a79b871-c28c-38df-8dd7-3490a6708070 | -11.66152 | -57.25389 | 2026-06-27 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9b08068b-d1da-376e-8e6a-24b936a7730e | -12.51741 | -48.28421 | 2026-06-27 04:32:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e5754d5-7e1d-3bab-b52a-6a010ce0caea | -10.48686 | -47.07854 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fe9e246-f43a-3ffc-9ee6-4dc027c874d2 | -10.54938 | -46.24387 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3755caa-76e7-33e1-8fb2-cc175eb979f3 | -10.13027 | -52.11361 | 2026-06-27 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 639d79fc-7821-3eba-ab0c-2ab9f45711e0 | -14.84961 | -48.14659 | 2026-06-27 04:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7308c48-5126-317d-8321-bb15e61d3fc8 | -10.48962 | -47.12553 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4765f447-942d-321d-a371-119ad5ae9459 | -11.9113 | -57.40656 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aae3e899-248c-38fb-8368-0ed61019c553 | -13.2661 | -54.40901 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f1c4c0c-d464-3ecd-aaa7-b5ed38ff10ab | -12.61901 | -57.89138 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 72aff0a1-6181-3ed6-aa34-ea8e73d276e7 | -10.47419 | -47.11589 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| becb6999-d2cb-378c-afeb-61f7a8de10e3 | -10.48191 | -47.13144 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d96fd2ff-1c0c-3540-bb45-602185a5a0d1 | -10.56439 | -46.23531 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92f971b6-c611-3e16-86c2-fe404fe3d60d | -12.45752 | -58.49324 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 50eede20-9415-3ca6-956f-9b8d8280b102 | -12.51685 | -48.28775 | 2026-06-27 04:32:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce8e58e3-6744-3427-829b-edaa761643b4 | -12.62531 | -57.88875 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c881290-9c1d-3869-8a7f-9bd718d641c7 | -11.31843 | -54.46175 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70b9d935-90d1-3dd0-8e70-77a217d5c791 | -10.54002 | -53.71094 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4626eb0-00a6-30a7-b3ea-de436b7a10c8 | -12.45033 | -58.49649 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ede87294-9efa-3e0c-ba50-7abac476ab7d | -13.26447 | -54.41778 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ac9168b-f52c-3f6c-a07d-8d160f897de9 | -11.91017 | -57.4096 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d19f860a-319f-3f75-be71-7c5483da18d6 | -13.43657 | -47.86687 | 2026-06-27 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a668ced3-ae69-3568-b868-345b1111738b | -10.65875 | -50.23076 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48f30022-14c6-3500-879a-be9cd5b35482 | -10.13116 | -52.1084 | 2026-06-27 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad5a07de-765b-32e3-915a-dcd999799dfe | -12.61977 | -57.88753 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 61fa7178-ee7f-3781-ad32-2845bbe39d4b | -10.66758 | -50.17781 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ff12d10-f6f3-3017-abad-9842e64f0421 | -13.26173 | -54.40812 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 541c43b9-5a62-3ff0-9e49-d009ba60dbbe | -13.24863 | -54.4055 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bfcc3b58-c066-3be2-bccf-995a03e6a91f | -12.44782 | -49.58167 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06002afb-1128-3f99-9825-7f26bc1876d3 | -9.07073 | -44.76624 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74c80548-3f16-3e28-a0d8-f226f6331112 | -14.69572 | -46.14632 | 2026-06-27 04:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13199604-2097-3ea4-ade9-41b1e7730e51 | -13.66223 | -53.93718 | 2026-06-27 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5d02f4ad-be72-35e0-b163-687681c6666a | -12.07888 | -54.61522 | 2026-06-27 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f973c2ba-1888-3b11-90d0-6c20f7474006 | -9.07419 | -44.76675 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c736481-1ed2-396b-8327-ea60745297c0 | -11.90469 | -57.40858 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e1e68c51-7570-32a2-8e6b-7a1824c8e7a1 | -12.16863 | -59.75445 | 2026-06-27 04:32:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be69b3a6-0865-3aad-bf58-cad7f3d57a22 | -9.13902 | -45.28532 | 2026-06-27 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 274f65e3-1bca-3000-8fcd-2d8c31911f12 | -10.55605 | -46.24494 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README14.md)
