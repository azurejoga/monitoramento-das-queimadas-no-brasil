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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7fd6b24-3b49-32fd-af05-c75fbcd1a25c | -19.6182 | -57.009998 | 2024-10-18 01:37:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 08dcf273-b318-3655-bd40-c4ece4ee58a1 | -19.6007 | -56.980801 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 188e94d6-2fc4-33bf-9bd5-eed6ad8aba1a | -19.6033 | -56.991402 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 85a2d62b-82fb-363c-b36c-6732f8b9e0f5 | -19.6059 | -57.002102 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 860e27fb-98fc-3d1b-9ad9-d0da54006e51 | -19.6085 | -57.012699 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fb21f9a7-82e9-31ed-aa0f-908597b68b5e | -19.6112 | -57.0233 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0e2a8686-9bdd-34fb-985e-ca52823e4f8d | -19.6138 | -57.033798 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 167526b0-4975-332a-b187-f7f4c509221f | -19.591 | -56.983501 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 15216d7f-331b-3f52-995f-d31da77bdc93 | -19.593599 | -56.994099 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 60422c3f-3549-39c4-9462-f48857114716 | -19.596201 | -57.004799 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e182950b-99ff-3386-91a6-c39b0806c989 | -19.598801 | -57.0154 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f1239c1a-2007-34f3-bad1-ab9676d31774 | -19.6015 | -57.026001 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 20456e15-d3a2-33bc-a9b9-d80bbef63964 | -19.604099 | -57.036499 | 2024-10-18 01:37:06 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c338ddb7-b34c-39bd-8e82-982426ba849a | -21.9662 | -49.7186 | 2024-10-18 01:37:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| 4e2e48ed-86fe-3a59-ada9-50e4814df93c | -23.3701 | -47.3747 | 2024-10-18 01:37:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 071f43f0-6bfb-317c-87cf-8d7b856d7682 | -18.6845 | -57.344398 | 2024-10-18 01:37:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| faa79757-47e9-3136-9374-8fcd5f556a0e | -18.687099 | -57.354801 | 2024-10-18 01:37:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5530fa44-8d6c-3f67-9400-4b03b06fb3d7 | -18.657301 | -57.318199 | 2024-10-18 01:37:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 96a55575-cae4-35fc-bdfa-ccc096d73d97 | -18.659901 | -57.328701 | 2024-10-18 01:37:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0f0d0bc7-5b73-3f6e-bac4-0b832b857f16 | -18.662399 | -57.3391 | 2024-10-18 01:37:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ee61909a-989c-333b-a756-f346d682c9ee | -18.637501 | -57.153999 | 2024-10-18 01:37:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bfa88da3-a9a2-3389-b0a8-cc4e0d5531d2 | -18.263901 | -56.611599 | 2024-10-18 01:37:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 29ac125d-31fe-3f43-b8a6-12ec126d13ba | -18.251301 | -56.6026 | 2024-10-18 01:37:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 871f3588-b985-3939-b126-d3601cc0e75b | -18.2542 | -56.6143 | 2024-10-18 01:37:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5ae27028-1fc1-38e3-ac73-98ff5f35aeeb | -18.257099 | -56.625999 | 2024-10-18 01:37:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a4cf3e40-04f6-3142-aec7-3d3e8c53297c | -18.244499 | -56.617001 | 2024-10-18 01:37:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0906d941-5756-39b6-960b-594caa271a20 | -18.2474 | -56.6287 | 2024-10-18 01:37:26 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 626fead3-0e9a-3995-8bf8-5bf711aad4bb | -18.208799 | -56.847801 | 2024-10-18 01:37:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0adfedee-bf2f-3873-853a-daa67bc45c6c | -18.211599 | -56.8591 | 2024-10-18 01:37:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fbab454a-b82d-38ff-968e-259a9cdeb629 | -18.072201 | -57.341702 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e731ed54-aa5b-3d3a-8b91-4d352fb53716 | -18.0131 | -57.312099 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3405ffbd-9c2a-3cec-bb3d-0ecf8f642c49 | -18.009501 | -57.255798 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 150d4e64-ed74-3721-8032-885e615228c0 | -18.012199 | -57.266499 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d0935e97-25e8-39f5-bf6f-fd5113663886 | -18.0149 | -57.277302 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 473815c2-f8f5-3474-9643-e516636588e5 | -17.9891 | -57.215199 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3ced7d3a-cf37-31fa-b477-bac52b9151e4 | -17.9918 | -57.226002 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 04b18d7e-79c8-3a21-a8ea-ffa9bdb3c845 | -17.994499 | -57.2369 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2574c0f4-a6b0-3c31-8a2c-c1755bd183ac | -17.9972 | -57.2477 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6c4ff22b-382f-3767-8cef-a791a3d6da39 | -17.9998 | -57.2584 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0ff8efb8-a71a-3e70-9f64-d5816327be6e | -18.002501 | -57.269199 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 45f4146e-c033-3263-a903-0df3b7376b5c | -18.005199 | -57.279999 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5b227dd2-5f01-3e0e-a02c-08c48723850c | -18.007799 | -57.290699 | 2024-10-18 01:37:32 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 72e54264-83bb-3328-b99a-346f61c16029 | -18.000799 | -57.304001 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e68a34b3-b27f-3360-92a7-996c7e5f1825 | -17.990999 | -57.306599 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fe43cdff-b4b4-3cb0-a512-fb906cc6cc2b | -17.979401 | -57.2178 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8237e777-127d-3f6f-9c7b-806b8260824c | -17.9821 | -57.2286 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 023611be-77cb-3b80-82be-eadfa4415bc5 | -17.9848 | -57.239498 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c8d238fc-69a3-334e-b295-fd6444faec35 | -17.987499 | -57.250301 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1d5f2405-2892-304e-8146-75d2adddb958 | -17.990101 | -57.261002 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44bb43c2-b541-3bee-8f42-60b3384e436b | -17.9928 | -57.271801 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc58b9ec-9a66-3ebc-a7f0-eb8a2efeb512 | -17.995501 | -57.2826 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| afbc78bc-8481-3cc3-b5c9-c89149afcca9 | -17.9981 | -57.293301 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 55fde902-5678-3e0f-a526-1a67a40cb201 | -17.9723 | -57.2313 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7af24a92-8fd2-39cf-a406-e09b5af0a226 | -17.975 | -57.2421 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d91f5071-0405-3894-9971-dedf94f3c0fc | -17.977699 | -57.252899 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2529be8b-8fee-3144-b85a-29e786f0856b | -17.980301 | -57.263699 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 49396369-b902-3e48-a7b7-26a836eec040 | -17.983 | -57.274399 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 198ac6e9-fb04-35bf-8484-edc81f8970c3 | -17.985701 | -57.285198 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f9d60b68-f5dc-3121-b503-f4b5ac06fa1d | -17.9883 | -57.295898 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c7d733b-e315-3ba3-951e-8611674eb3b9 | -17.962601 | -57.233898 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac536758-4b08-3980-9429-a325c3938978 | -17.9653 | -57.244801 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8f99ad30-7539-320a-8025-0560c9030a55 | -17.968 | -57.2556 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8f4ac25e-3fd4-3340-a6bb-8ed230a49a80 | -17.9706 | -57.2663 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b75c107f-7415-3fe3-968e-b909395d256c | -17.973301 | -57.2771 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0bc83e79-e6dc-3ff0-b22f-8525e16d8c87 | -17.976 | -57.287899 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6a996ad1-9254-3f9a-8d70-06468e61c411 | -17.9529 | -57.2365 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7627cb25-2b6b-3a85-8e04-e04d78ba3347 | -17.955601 | -57.247398 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dc1f8d4b-510e-3e4d-b6ec-b9d0e3e29140 | -17.9583 | -57.258202 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 76882a45-8445-3799-a86f-668460adc23a | -17.960899 | -57.268902 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1baea1e1-a922-3b75-810b-d5a885fea0db | -17.9636 | -57.279701 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 51385ed8-02a1-33ad-bdc6-8dd6f3db8a2c | -17.943199 | -57.239201 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fa1d0f57-df51-30a0-bbba-f173f5ba5586 | -17.9459 | -57.25 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d8e68f16-8731-3183-95a0-1ef80bc7ddd0 | -17.948601 | -57.260799 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8b283d10-06e2-30af-b719-ef77a51c7d72 | -17.9335 | -57.241798 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 35032bc4-a1cf-3e6b-b30f-26ec06fca172 | -17.936199 | -57.252602 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ae8d8acd-9ece-320a-b745-fdddc2ca1f15 | -17.8601 | -56.821499 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 52302ac1-db7d-3718-8581-2a14cd1ea58c | -17.863001 | -56.833 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ea916384-1f46-3c65-b1d2-e73050efd968 | -17.8715 | -56.867298 | 2024-10-18 01:37:33 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2e3646a4-e38d-3fbe-84da-2e29feea61cc | -17.9492 | -57.431301 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5648f848-b7b6-380c-b677-b2eb15690c73 | -17.951799 | -57.441898 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 324d14f4-5945-3e74-af10-c3b4b999f5dc | -17.929701 | -57.4366 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 957895c5-f8a8-3296-a19e-fc0c218b87fd | -17.92 | -57.439201 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 86e623b2-ccf2-337e-ac1b-35c693151ef0 | -17.9226 | -57.449799 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5363cf10-d598-3c3f-b784-d486174cb394 | -17.9114 | -57.236301 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e39a5ac9-48fe-3d71-b84b-20200b847524 | -17.914101 | -57.247101 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b7fa8a2d-5f36-33ad-a7fc-3fae1f35f761 | -17.9016 | -57.238899 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 00ff5121-af68-30c1-99aa-e20ecf10c4e0 | -17.904301 | -57.249699 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ccf68736-569a-3505-ba1a-4d40cf97b57d | -17.8866 | -57.219799 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 409a6118-6288-30c3-93de-1b02a043cf6f | -17.889299 | -57.230598 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc0df26b-c5a7-3ee3-b628-c89f2391221c | -17.891899 | -57.241501 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 10fdc075-ae9f-3280-95fa-60ad6d4d60f1 | -17.8769 | -57.222401 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bc92e89d-19b3-3d80-92ad-0de7692eb593 | -17.879499 | -57.2332 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9656a344-738b-33b7-8831-eaea518ea3cb | -17.869801 | -57.235901 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d184dea6-cf90-3ab3-9996-597b9b2c4590 | -17.872499 | -57.246799 | 2024-10-18 01:37:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4696b4b0-1540-33f5-849a-ed8cb819d583 | -17.910299 | -57.441799 | 2024-10-18 01:37:35 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 825509bd-9567-3ce6-b3b3-b135b88d8621 | -17.9006 | -57.444401 | 2024-10-18 01:37:35 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9d93ba6e-feb0-3077-bad9-d252f6695ecc | -17.9032 | -57.455002 | 2024-10-18 01:37:35 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f97ac599-efc6-3b24-9920-c831ccd810dd | -17.8601 | -57.238499 | 2024-10-18 01:37:35 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f20e5f5-a6ba-30b4-b121-b99450f77a11 | -17.862801 | -57.249401 | 2024-10-18 01:37:35 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f69d2a6e-4cd7-350d-8589-b5f7b722c59c | -17.8909 | -57.446999 | 2024-10-18 01:37:35 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README15.md)
