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
| 31f3ea94-3db7-3c68-8563-cbf467e64a5d | -10.93581 | -56.8572 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa72b81a-03a7-3fc4-9fdd-4daa894c16d9 | -12.44038 | -49.58426 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3af163e3-5406-348d-81f8-2c053427a08d | -14.69975 | -46.14297 | 2026-06-27 04:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32dede03-30ec-3d3c-9ef2-7996c85a0efe | -10.54391 | -53.71418 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c18e537-e201-395e-886d-abea047b870d | -13.94092 | -47.33439 | 2026-06-27 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7ead5ea-fdca-355f-9fc2-96b5156c2f60 | -15.58619 | -46.8078 | 2026-06-27 04:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6680d039-5568-30f4-bb71-5e6c2017bbfa | -9.06815 | -44.7662 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b70cb9b-08c7-330a-a98e-81aeb7123757 | -11.91086 | -57.40595 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62b7415a-aab3-33cf-a0c1-85b3350a3990 | -9.47548 | -48.07227 | 2026-06-27 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85e243e0-2e67-35c8-8ca3-b1aee00cff5e | -10.77856 | -54.10117 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c4c099b-ee1e-3767-b10f-781f47db40ca | -10.38549 | -56.71796 | 2026-06-27 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03c2ad52-9883-3257-916f-ebc9badaaad8 | -13.94424 | -47.33492 | 2026-06-27 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c39d40a7-52d6-3bc4-8b6c-a915f9b8eef8 | -10.90074 | -56.85229 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c54f7bb6-1098-3a70-9d47-107218a069b2 | -12.79303 | -54.86681 | 2026-06-27 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d7d1c22-335f-31bb-9f29-b63507e5831a | -10.4775 | -47.11642 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e82df594-502e-3f91-8fe1-09ebfc72f8dd | -12.4619 | -58.49891 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a10cdd65-7f46-31bc-8b6d-4625297bc0ec | -13.22261 | -54.42332 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea8097ca-1c7a-3542-bce4-3aca73c76660 | -10.81169 | -55.86267 | 2026-06-27 04:32:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 942ab9b5-3363-3115-8f21-0f274a66f2c7 | -9.68971 | -47.69039 | 2026-06-27 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e6298c5-f3e6-36aa-abbe-43ac09597656 | -9.81993 | -48.2999 | 2026-06-27 04:32:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37372f17-1153-3a79-8e7d-0aab79275dc9 | -10.80609 | -55.86473 | 2026-06-27 04:32:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a45f43d-a7c7-30e8-a005-19287175a4b5 | -13.24426 | -54.40464 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e1e0f43d-d2d8-36e3-846d-92e86c5f9eba | -13.08915 | -48.17185 | 2026-06-27 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03e1b432-5d59-3cdf-9e83-be8a4cae4912 | -9.59617 | -56.92601 | 2026-06-27 04:32:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fece6a0b-c06a-3a3d-86e7-6188db6a535d | -12.4592 | -58.48466 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 241f9b07-00b1-3e94-8b31-5cf4378475fc | -10.77777 | -54.10564 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1f84cd1-279a-3b7e-95ad-77863af4b65a | -13.45254 | -47.87312 | 2026-06-27 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ccf7b96a-10d7-3ac0-8a73-2a34719357e1 | -10.39011 | -56.723 | 2026-06-27 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf78a9fc-4779-3db0-b956-c132923ed02a | -12.46366 | -58.49024 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a71eeaa3-6b2e-3690-b9a1-eb4d24e2fa2f | -11.90366 | -57.41652 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 659eba6c-317b-3960-88d6-b2a77ed4d7dc | -12.45088 | -58.49637 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8db52ecc-416b-3d72-99a0-7fe2d1d16f76 | -10.47859 | -47.08796 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd4ee379-f28f-3b53-b307-84ad310e934e | -12.52016 | -48.2883 | 2026-06-27 04:32:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2120b533-9c6c-3618-ab8b-044c31fde1f2 | -12.93921 | -56.646 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afe14d30-f37b-3c90-bc58-27f8eac277d6 | -10.1263 | -52.1129 | 2026-06-27 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea757949-5e09-365f-a501-de1ffc95674a | -12.61825 | -57.89524 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 47b46a22-f0eb-391c-a7e1-2c2f32d66812 | -10.93943 | -56.8535 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4409a14-b088-360f-bc65-3294cf753fc2 | -10.62529 | -50.2124 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0379da0-9d46-3f28-8bbb-55e5bae2e608 | -10.9372 | -56.85004 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3df19cee-e7c4-34b2-9667-ac0666d924b5 | -12.60941 | -57.88152 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fadbeb84-2711-33d0-b0bc-3cbbe25f103a | -10.33566 | -50.14467 | 2026-06-27 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a87aec1-497f-3230-8c99-157e56120c64 | -13.25736 | -54.40725 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e44c396-61ad-3e4f-98d9-ae1d8dd4f6b1 | -13.2478 | -54.40992 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb367570-6749-387c-8f68-10eefc1daa9d | -12.79391 | -54.86202 | 2026-06-27 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30567034-51ba-395a-94d4-b4c9722e153a | -12.45612 | -58.49771 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| dba2cd08-be48-3f31-af16-7021532b0b9d | -13.60566 | -56.59605 | 2026-06-27 04:32:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a68f1da-25bc-3d9a-a896-663f197a08da | -11.90986 | -57.41387 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18c55d63-d8e8-3526-a242-89a34110c75c | -11.90876 | -57.417 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d967bac0-1d82-3316-8441-3389b57a540b | -12.45874 | -58.48479 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e4cc93e2-e9ce-3dd8-a304-c3a3955dc6e3 | -13.8354 | -47.13719 | 2026-06-27 04:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35e8b9fb-3597-397f-b7ad-7459cb009f53 | -10.11891 | -48.25673 | 2026-06-27 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ade1d14d-af29-3567-b99b-f0ba958c47a4 | -13.22307 | -54.42203 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7dfb433-6eec-349f-9a6d-f943e0b0ab76 | -11.05249 | -52.46165 | 2026-06-27 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7041b9b0-f3e8-3712-94a8-0aa33ec44cb0 | -10.47915 | -47.12742 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ed4ab49c-302b-3237-941f-0981f69b5180 | -10.90543 | -56.85692 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fc814e1-2bd0-32dd-9759-aa7606bb79bb | -13.0864 | -48.16776 | 2026-06-27 04:32:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 737e0453-1018-3f1a-9eaf-f0f691b98809 | -11.904 | -57.41221 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9977dc0c-e89e-3bdd-8a9e-4bd0640ebf9c | -12.67394 | -48.21898 | 2026-06-27 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05e6af86-f4f2-389e-8bff-93b7b8bc475b | -13.93815 | -47.33026 | 2026-06-27 04:32:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 364ac517-32e1-309e-b291-ad8bab0b12fc | -11.64947 | -54.89399 | 2026-06-27 04:32:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0736c86f-9279-371c-9344-b3f7031113cd | -12.55469 | -54.59171 | 2026-06-27 04:32:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe0eaac1-1f75-3045-aef6-5d8f7fb07de1 | -14.87612 | -54.53048 | 2026-06-27 04:32:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9978f896-5346-3beb-bd77-f7f29f101351 | -10.90478 | -56.8604 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14559af7-431f-3cc0-b6c9-69f697e054de | -13.86707 | -50.39807 | 2026-06-27 04:32:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ea8971f-db6e-3237-81f4-2d31cfcffb4d | -11.90511 | -57.40918 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4e7a6bb-a88d-38f1-ac71-d8e89cb39ff2 | -13.94147 | -47.33079 | 2026-06-27 04:32:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbba66d1-3215-38f3-a96b-d8662c3fa537 | -11.32296 | -54.46264 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7668e030-7414-3abf-9708-09eed42e378c | -8.86682 | -46.92511 | 2026-06-27 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc50a543-6edd-3a97-b147-62107a24ecd9 | -11.88226 | -57.81728 | 2026-06-27 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06b0c441-ab12-3ae1-8d0e-16f5bd090780 | -10.53953 | -53.71338 | 2026-06-27 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5cc7401a-8901-30b3-8c2b-628c05364d08 | -12.45259 | -58.48763 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 63903d21-090f-3eb6-bedf-9a5f4cbd10a2 | -8.71433 | -46.96447 | 2026-06-27 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa8e3f63-1eae-3d47-a57b-3a44a400a370 | -8.86958 | -46.92911 | 2026-06-27 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4717136a-f3a7-3ea8-bb84-adbbfd0a1b86 | -10.48466 | -47.11399 | 2026-06-27 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ca45f45-ff3d-32f1-874a-2c01e8644237 | -11.04848 | -52.46097 | 2026-06-27 04:32:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 039e711a-8c59-3bf1-9453-49a2c0b46f95 | -10.4764 | -47.1234 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc5abaea-4881-3f45-a146-f39d9e0a1613 | -8.8536 | -46.92299 | 2026-06-27 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6eefbd5-299d-3a01-8c78-214824737651 | -11.91239 | -57.10487 | 2026-06-27 04:32:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16096cae-d823-3c91-b409-ae13234d6a96 | -11.90912 | -57.41759 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e387c702-37e2-379c-8da1-8503e009e089 | -10.6246 | -50.21648 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afd32442-974c-3689-a4cc-2132a3adf749 | -10.62884 | -50.21301 | 2026-06-27 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c0600b-67e8-33fa-ad68-26345fb6d4b7 | -9.89936 | -47.03386 | 2026-06-27 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a52b32b-83b1-3fde-bcd4-3c6447a7988e | -12.4633 | -58.49448 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| b24e0cc8-819c-3ea7-82a2-192dee43cdbf | -12.60864 | -57.88536 | 2026-06-27 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7a068913-a361-342a-a63e-5defe735d5f7 | -13.44043 | -47.86388 | 2026-06-27 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4f98e2d-bfa3-3a57-8675-febeb6da1e3b | -14.69858 | -46.15073 | 2026-06-27 04:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44ec819c-f05e-3307-8750-aa07322096d2 | -12.44503 | -49.57734 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb909abd-127a-3875-947c-b95fb221bd12 | -13.66149 | -53.94122 | 2026-06-27 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6e671c01-7ae0-38be-90b8-3fc7193f9444 | -9.47605 | -48.06873 | 2026-06-27 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00472534-37b5-39c7-b57a-cc958a6589df | -12.44441 | -49.58109 | 2026-06-27 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cebafe98-2c13-351b-85a2-b2255c1443b9 | -12.46415 | -58.49014 | 2026-06-27 04:32:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 8502da83-6d30-3161-b12f-b573747c8b87 | -9.07476 | -44.76295 | 2026-06-27 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ed30da6-5f7b-3b69-9358-5ccccb04b133 | -12.2225 | -56.5627 | 2026-06-27 04:32:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d1f3468-831d-3afc-b99d-926d42ea5009 | -13.60507 | -56.59903 | 2026-06-27 04:32:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d111a2eb-00f8-368d-bb32-a2ab91d11d5e | -13.22745 | -54.42289 | 2026-06-27 04:32:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b2f6f96-bb5e-32fd-9efc-50d655dc9447 | -11.91532 | -57.41498 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23e88fe6-c961-3fe2-aa33-693bb4cccfb1 | -10.30558 | -57.14386 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4be20a10-1792-3607-b7e8-a2a29ed83f46 | -10.47694 | -47.11991 | 2026-06-27 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| de0972bc-e1ca-3e70-a540-ac0cc3856ab0 | -13.83485 | -47.14076 | 2026-06-27 04:32:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e347d512-a8fa-33ff-9055-5551ff3afcb5 | -12.93981 | -56.64289 | 2026-06-27 04:32:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
