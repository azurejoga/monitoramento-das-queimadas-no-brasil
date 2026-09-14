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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24460780-3332-3cf3-81f9-d03211b83987 | -10.67924 | -54.16035 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 1ba5df47-c1c2-347c-a464-bad73356cc5d | -10.68282 | -54.13015 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 542a3858-a02d-375e-9a71-9649f1e703dd | -8.54311 | -54.70551 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f73ad774-84ba-3bc4-bd4a-61b7799c5dc7 | -10.96147 | -58.95842 | 2026-09-14 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5eda0784-ae9e-30d2-9304-09e83e43b564 | -10.68073 | -54.1113 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bb4810d-0fd5-3a3d-9b40-5adf8231aa57 | -10.68408 | -54.16979 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91ab4df5-d4ad-319b-958e-c6b46f456d6c | -10.6813 | -54.14298 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| de1a8456-0c48-36de-b0ba-17cba11e9795 | -10.54779 | -51.3103 | 2026-09-14 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f756f298-9007-3382-a4f1-f440b09f4911 | -10.68819 | -54.13529 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16f5c13b-f9eb-3015-8739-47cd885a4b81 | -10.67481 | -54.15837 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 35c60964-db83-321a-b93f-91b8b0916043 | -10.65929 | -54.13909 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f7cbb6e8-9c07-32b4-bf5e-1548f30e944f | -9.79869 | -55.30963 | 2026-09-14 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 205a3df8-9229-3f08-a0c1-94b1317bb0cc | -10.0362 | -52.12735 | 2026-09-14 05:38:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9fd0d77-9920-3ae6-900b-cf1e2afc0f4c | -10.54856 | -51.30319 | 2026-09-14 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 61c07eb6-b36b-3aaf-b837-d8e4996f0518 | -10.67214 | -54.13199 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4b31e6a-845b-31d5-ba58-4acf5c0cb70b | -10.68308 | -54.17823 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83e42945-efd8-3227-ba0f-273015e1cb50 | -8.5381 | -54.70094 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d37a1646-cfa9-3e6d-9f4f-efc075449111 | -9.68897 | -54.84253 | 2026-09-14 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f7667da-2121-3184-8f24-af3a605b4e8f | -10.68287 | -54.14188 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f3c30f9-9407-3818-a9c7-0479039e0eaf | -10.54712 | -51.31649 | 2026-09-14 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab20a125-5106-33be-bc52-f95a6f1ea6e7 | -10.68394 | -54.13338 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3da695ee-6114-3e92-aa99-06d2e71dbfdc | -10.69585 | -54.17125 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4873fc1d-c967-34dd-a4ff-2fe4d9841fb7 | -9.59178 | -55.153 | 2026-09-14 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce28d83a-ad4e-3642-81d4-1118b3992d1b | -10.67321 | -54.12349 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e89af137-b54e-3277-87d6-94c2f4d2be2f | -10.67997 | -54.10359 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ac19ffe-9167-3ab0-b52d-ec8ec882cde7 | -8.54813 | -54.70996 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf3a7f23-5c79-36bb-b6e9-8f44bb6da629 | -10.66259 | -54.14954 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e2504707-50bd-39b4-a973-549147bbdc60 | -16.2316 | -52.65423 | 2026-09-14 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9df319f-80a7-378e-8cf8-f7b23913759c | -10.68871 | -54.13097 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e42cc66-74e2-3d1d-97f1-27ba967f404f | -9.25563 | -60.28255 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98663a95-861e-36bc-8137-f40a488335d3 | -10.68233 | -54.14613 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bef5062f-7acf-370f-9335-7a45dbb458da | -10.67374 | -54.1669 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d5ad48e9-83a5-3064-9568-7fbbff536668 | -8.77199 | -61.39918 | 2026-09-14 05:38:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e307660d-6786-3a29-b0b6-f51d8ea96c9c | -10.96575 | -58.95898 | 2026-09-14 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b95cf5f-8248-3ce4-9a38-8ff504707479 | -11.3919 | -58.33033 | 2026-09-14 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be1ccbed-77df-3dc0-9518-caecaa2a5720 | -10.66849 | -54.15019 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c84ad68b-478b-3943-bd00-4f2f71c00a2f | -8.53761 | -54.70461 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26f53d2e-8777-378a-8f5c-6d400ed0e67d | -10.68459 | -54.16556 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3385c13c-09d5-35ca-a78c-565e6985ce31 | -10.67961 | -54.16773 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f6a5f279-f3d3-3794-8ce4-63de9b320551 | -10.66571 | -54.13556 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0b1cd2e4-b0d2-3933-bdca-871c12afa90f | -10.66361 | -54.14086 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 1eaed7a6-dca3-3591-82ca-c01038ebf8e9 | -10.65232 | -54.14703 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5e61f78c-38d4-3dff-96e6-86fa6baa2348 | -10.68535 | -54.10885 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd1e920e-0bd2-38c9-b383-3af0491ca546 | -8.93622 | -61.45929 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91c5d6db-5a48-3e07-8d10-8f95205711c1 | -10.67001 | -54.14903 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 281.6 |
| 0ca63fc9-bc9a-3c49-924e-b81f1d808bf4 | -10.67051 | -54.13307 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| a57c1700-6184-3265-8339-cdc762f0ab57 | -10.66208 | -54.15394 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c3ad5884-e09b-3a71-9e75-f5dea76ebc92 | -10.69149 | -54.15779 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bfacb57b-5244-380f-8d7c-8b08c1fbf60b | -8.54459 | -54.69431 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9c5946a-584c-3f91-8238-8ea9e9af3d46 | -10.65822 | -54.13588 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 44f43b8b-70c2-3ff2-bd31-cc5a20ffa2bf | -10.69201 | -54.15343 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 98e4c45e-0a8b-39f7-bc18-752ec6fa2984 | -10.6759 | -54.14974 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b0453b87-bfac-343e-a9c2-084c5700a73b | -10.67693 | -54.12939 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 204713aa-0807-397c-9a5d-9f226721a5da | -8.53713 | -54.70827 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45c9b9f0-b67c-3e5e-a250-07ab53db8684 | -10.81005 | -58.58324 | 2026-09-14 05:38:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 338acb48-8ec2-3c6a-a3b4-c5b5cf3694ec | -10.81063 | -58.57898 | 2026-09-14 05:38:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9864d89a-342b-3957-b4c1-1eafe7dd6d2b | -10.67751 | -54.13687 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 980dd089-65b6-3b9f-a80c-28645d607991 | -10.66798 | -54.15454 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fc89c68f-4529-34bf-b405-1cb80c919d0e | -10.67642 | -54.13369 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8772df5f-62f3-39c6-a599-1131b2c87f27 | -11.26272 | -54.12561 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc77ad38-d25d-3f4e-a19a-922412ebce6b | -10.67235 | -54.16805 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| fc39604a-1684-33b6-ad42-2479ee843865 | -10.6625 | -54.16129 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cc3da9f6-9459-394c-9ff6-a893fd749843 | -8.7136 | -62.56427 | 2026-09-14 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1fa67813-a8df-3f2d-b8b8-47c4bf4636f0 | -10.66411 | -54.14838 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 281.6 |
| e42114e4-eb02-38e8-a3c0-d43d9f9bcca4 | -10.6851 | -54.16129 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38e91829-2ada-36a9-9202-5599681c6e69 | -10.65875 | -54.14338 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b29c8421-c405-391b-aa10-479dae41c7ad | -10.67859 | -54.12829 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10096ff1-f6d9-35f9-b105-d6c064651238 | -10.67946 | -54.10793 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2f9d85c-0360-396d-80a5-548d87e7bc0f | -10.68014 | -54.16348 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d36c4116-6feb-3e7e-a549-d5590bafc7e4 | -10.68718 | -54.14375 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b653ff6-b8b1-3933-98a4-f14bebfe7519 | -10.68483 | -54.11319 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5199b53-f592-32bf-b3a7-d1b3aa7224b8 | -10.66697 | -54.16309 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4035067e-cb88-31dc-a137-6e3d16955308 | -10.68606 | -54.11652 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78ccd700-e077-37e8-8e5e-5fa3da98ca97 | -10.65767 | -54.1521 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2417b254-138f-3a8e-8103-2b23e3db5eb5 | -13.31827 | -51.71767 | 2026-09-14 05:38:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25637b50-4a89-37e5-9bbd-401fa1c02fc5 | -10.66839 | -54.16191 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 242a26a8-ab55-3882-849f-b1c0186f7af4 | -10.67387 | -54.15522 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 249.6 |
| 635f5025-f20d-3f4f-8ef7-67330f25dc1c | -9.59221 | -55.14977 | 2026-09-14 05:38:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24876860-1b21-387b-9320-d1a5b8b76a04 | -10.67771 | -54.17316 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1cdc3c9f-29c3-36e6-9b13-7a0beb265812 | -11.3925 | -58.32583 | 2026-09-14 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be99362e-5431-3dfe-adda-98f25b702f52 | -10.67895 | -54.1123 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96253b86-1a01-30b5-85ae-4edfdb0f8030 | -10.68946 | -54.17478 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4472d8e8-9e1a-3ac1-aeb3-696503efb81b | -10.68068 | -54.15919 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 5f1bf7aa-46a3-377f-9b42-08b81ed50be9 | -10.66893 | -54.15763 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f18911d7-7c51-3556-9182-a0b7daf9128c | -10.68586 | -54.10452 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f59d978a-2d9e-3cad-b1e6-c280238e2749 | -8.81435 | -61.4097 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42336aca-47b5-33b9-9353-9dc7aee5f675 | -13.32527 | -51.71874 | 2026-09-14 05:38:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f13db2e-a26a-3871-aae1-dbc105e63fdf | -10.68921 | -54.12674 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 017d97e3-e58f-3920-ad47-8b704bc00f46 | -8.93682 | -61.45517 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 53e2da5d-8eeb-32eb-a2c4-1d89169d2858 | -9.17387 | -59.42223 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b4c645e-d9d4-3f95-aefd-874f00859cc1 | -10.6877 | -54.10353 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5560ecd9-8ae3-3c97-8676-bee20be666db | -8.53616 | -54.71561 | 2026-09-14 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fda7206f-808c-33b4-926c-387b11fe4fe6 | -9.17437 | -59.41866 | 2026-09-14 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 696602f7-fc8d-3cae-b607-502d3504f37a | -10.68332 | -54.12598 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fed414a5-e5b2-3a72-9f0e-1bf15c457aa8 | -10.68127 | -54.10694 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1641fb2-69c3-3662-a7c5-31f95ca755af | -10.67805 | -54.13257 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be6cc15b-7946-35f6-8dd7-32b45abf2928 | -10.69534 | -54.17548 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b1e2b28-1385-3a81-9dd5-94e9987d3182 | -10.66465 | -54.14404 | 2026-09-14 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 281.6 |
| 11df5b36-6969-3109-9b16-91c5b6d011e9 | -9.70767 | -54.37538 | 2026-09-14 05:38:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7e0fce25-0b62-324e-a734-b5b077469a47 | -10.54154 | -51.31457 | 2026-09-14 05:38:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README60.md)
