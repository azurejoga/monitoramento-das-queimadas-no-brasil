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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a4290d0-8fc7-3163-8115-562fb7ff15ce | -14.4138 | -43.9672 | 2025-10-09 01:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 317.0 |
| bb8cb646-5672-306a-bf3b-da57f79dd5d9 | -7.7755 | -44.0396 | 2025-10-09 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 1d65acaf-ce84-3ec8-8ed3-f6f8a759afdd | -6.6808 | -46.2961 | 2025-10-09 01:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| fe6fc5b5-dcad-324f-844f-94df691bba77 | -4.9908 | -45.1351 | 2025-10-09 01:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 9a747ce9-5427-32b6-9637-7c2b859ef5dc | -9.0829 | -47.9594 | 2025-10-09 01:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 46428c95-3001-317e-8540-c8a3dc2fa1c9 | -13.6442 | -51.7282 | 2025-10-09 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 86c3adef-a1ce-3bc7-be1c-80a529af5cac | -5.7369 | -47.4681 | 2025-10-09 01:00:00 | GOES-19 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 358213a1-dbb4-36a1-8b15-3359e3459706 | -6.6993 | -46.3169 | 2025-10-09 01:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 934f2a05-db04-319d-bbc4-628afb460c49 | -16.0008 | -50.9892 | 2025-10-09 01:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a15ab695-9366-3baa-b927-50ba1ef26c73 | -14.4329 | -43.9874 | 2025-10-09 01:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 82f09358-1187-3ce8-95bc-1f30b363fe67 | -18.9974 | -43.0805 | 2025-10-09 01:00:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 166.8 |
| 98a624f1-55c8-3d8b-9ed3-da9ba1b6e44e | -8.1993 | -43.3424 | 2025-10-09 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 1a6d64f8-f3cd-3b18-a2f5-5bdf11c0f527 | -10.8505 | -49.9217 | 2025-10-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 3a6e7546-03ae-3c19-9089-6e059ddd17b7 | -10.8695 | -49.9196 | 2025-10-09 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e5e2da67-ab44-3556-a09e-ef2ef1b203d8 | -9.1718 | -46.9123 | 2025-10-09 01:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 51f18b91-0259-3487-ac59-f18e9b0f20b0 | -14.4133 | -43.9911 | 2025-10-09 01:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 929252aa-a96a-3464-a6c5-6a778cc7ed53 | -7.7567 | -44.0415 | 2025-10-09 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 3b2843d3-8137-34a9-811b-f7cf02580fbb | -4.9708 | -45.317 | 2025-10-09 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7f632f3b-2862-3429-8dfc-e3617568ff48 | -18.4118 | -45.2394 | 2025-10-09 01:00:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a673a13f-9d11-328c-8ca3-3ad81726dbd2 | -7.7569 | -44.0183 | 2025-10-09 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 1a297eb7-83eb-3c17-ac39-bf5ee49f64ef | -9.1018 | -47.9575 | 2025-10-09 01:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 50c12fe8-9ec7-30ea-8934-94ec7dda983a | -18.9771 | -43.0858 | 2025-10-09 01:00:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| 0671ac2e-a710-3ab4-95c8-609484874a6f | -18.0213 | -50.4547 | 2025-10-09 01:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 3950e29a-8ef4-3129-b8a4-4b547175789a | -13.7909 | -45.8552 | 2025-10-09 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 7cadc7ec-3f87-349f-bb6c-8684b0549811 | -18.0653 | -51.1522 | 2025-10-09 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5cb00c91-3523-321f-a201-6fa3882ac01b | -18.0448 | -51.1777 | 2025-10-09 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ab7deaab-32f1-34c5-86b7-6b9bbac44faf | -6.6995 | -46.2946 | 2025-10-09 01:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 8e2cdc53-884f-36a8-95ab-4b118b68a8ea | -14.4717 | -52.8937 | 2025-10-09 01:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 36f1cc82-7d11-371a-ae7c-319fca4e7f44 | -8.5024 | -46.1995 | 2025-10-09 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| bc0641c4-dc2e-33fe-a373-c20239eaacf1 | -18.0453 | -51.1556 | 2025-10-09 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| be664dc5-fcb1-3a35-b705-7bf93378ee6a | -17.8413 | -57.6459 | 2025-10-09 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| a0930862-8e7c-31d4-8fa7-459374683c07 | -5.4413 | -44.8335 | 2025-10-09 01:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 77d4e1b0-a5e1-3166-8c4b-87b6aaa3d028 | -4.9896 | -45.2933 | 2025-10-09 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 2cdd68f9-e18e-3c03-ba30-327ba7364fec | -6.6806 | -46.3184 | 2025-10-09 01:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 29d497cd-a871-3744-8fc1-06bc3f70bdb8 | -14.4334 | -43.9635 | 2025-10-09 01:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 319.7 |
| 2b589818-95d5-3c32-96f5-659cff9e8248 | -18.0648 | -51.1742 | 2025-10-09 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1e5cc2ff-949f-35a9-b377-31f7a8bafe49 | -19.7553 | -42.1994 | 2025-10-09 01:00:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| adf8de78-76de-3945-818c-d1e787ccb213 | -16.3757 | -46.3779 | 2025-10-09 01:00:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4d3d924e-98ea-324b-93f7-7c3948eaa142 | -4.278 | -48.8891 | 2025-10-09 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 92ac7eb9-11a7-34e1-bf65-3eb26bc14198 | -4.9894 | -45.3159 | 2025-10-09 01:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a1ea73ed-bea7-3bd7-a657-c8b532940368 | -8.5021 | -46.222 | 2025-10-09 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 9d1536cf-d790-3424-9eed-a080fbefd90d | -9.0832 | -47.9374 | 2025-10-09 01:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8ceff1c8-04ba-3e8f-9318-15c1f336ae8c | -4.2864 | -44.5171 | 2025-10-09 01:10:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 744c924b-a5c5-3476-8256-d5c1b6dd6946 | -17.3771 | -46.6636 | 2025-10-09 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2ba9db66-f8d8-3e5e-9299-e8c515b76f58 | -7.7569 | -44.0183 | 2025-10-09 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| bd82339c-4632-386d-8441-b08709894a87 | -4.9894 | -45.3159 | 2025-10-09 01:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0e43569e-6d93-3f8e-974b-fcf5b0ed1f84 | -10.8505 | -49.9217 | 2025-10-09 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cc57c394-6cbe-3543-aabb-a9f63a7f7216 | -8.5587 | -46.2162 | 2025-10-09 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| ade0550f-6b7b-3f1f-8220-46a4e6f21c67 | -8.521 | -46.2201 | 2025-10-09 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 65e8b240-051a-3c27-9b1e-877727b29b05 | -9.0832 | -47.9374 | 2025-10-09 01:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bca185c3-319e-3b43-8839-a69e3a632430 | -17.8413 | -57.6459 | 2025-10-09 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| 932abcc0-be38-38a7-8a0c-00af483c09f8 | -18.9967 | -43.1054 | 2025-10-09 01:10:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 6454ed64-bbf7-357a-a669-752d830606d6 | -19.7347 | -42.2052 | 2025-10-09 01:10:00 | GOES-19 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.1 |
| a267df8b-2fcf-37f3-aad9-2e0d4f3c3eb7 | -6.6993 | -46.3169 | 2025-10-09 01:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 79ac56a4-21dc-3da4-b2f1-f00f0efd5e8e | -8.5024 | -46.1995 | 2025-10-09 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| bd8a8bdb-4aa0-3ed5-b6a0-865dd1ef4df7 | -8.1993 | -43.3424 | 2025-10-09 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 42034648-17d2-37e8-a078-6bc7d66ade8b | -4.9896 | -45.2933 | 2025-10-09 01:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 07df8b10-f86c-3ccc-a72c-56a3b1388cc6 | -14.4334 | -43.9635 | 2025-10-09 01:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 262.7 |
| 4b60855f-78d8-3459-8b71-5576433d28db | -13.8121 | -43.9129 | 2025-10-09 01:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| c44dced6-92df-3516-afce-6b9fea3735a6 | -6.6806 | -46.3184 | 2025-10-09 01:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| dc39828f-5cfe-3231-835d-1b16b59d042e | -18.9974 | -43.0805 | 2025-10-09 01:10:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 200.3 |
| ad4cd007-0849-3591-8a91-e2bebfe93208 | -14.4329 | -43.9874 | 2025-10-09 01:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 43baeeb4-c7c2-3992-9792-7abe5e1413b6 | -13.7909 | -45.8552 | 2025-10-09 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| e030d9b2-86ac-3c8b-865e-f77130756950 | -14.4138 | -43.9672 | 2025-10-09 01:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 279.7 |
| 7da4ebca-cc22-3c21-85b6-1e8e2c9666b8 | -14.4133 | -43.9911 | 2025-10-09 01:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 22e00ee9-0824-3293-8a34-3c3503f9f50f | -8.5021 | -46.222 | 2025-10-09 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| cbd13341-d521-3291-b460-50df8706cb1b | -8.5398 | -46.2181 | 2025-10-09 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| aa2f5777-c23c-3d43-affc-f3f25e0e7360 | -18.4118 | -45.2394 | 2025-10-09 01:10:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 11f9c8f7-2a69-35ef-aa03-0306e08c9f0c | -16.3757 | -46.3779 | 2025-10-09 01:10:00 | GOES-19 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 655dec2a-1458-306b-9132-81500d2ea637 | -9.0829 | -47.9594 | 2025-10-09 01:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 63306716-0a4f-33c3-90fa-c63844809cd8 | -16.0012 | -50.9674 | 2025-10-09 01:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 51282d09-c0d4-386e-997d-4451963fa5ae | -6.6808 | -46.2961 | 2025-10-09 01:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 32aae495-8d6b-31a4-8702-54b30f3624f2 | -4.305 | -44.5161 | 2025-10-09 01:10:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a1d67897-8399-3874-bd22-f14653ad6e09 | -17.7137 | -40.2435 | 2025-10-09 01:10:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 93.0 |
| 1e0993e2-9295-387d-9b30-b8cae5650c11 | -13.8116 | -43.9367 | 2025-10-09 01:10:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| fe2c4f5f-116b-309c-bd60-d09438db4c4c | -6.6995 | -46.2946 | 2025-10-09 01:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 2ce44bf1-d8aa-3c4e-af55-fe06714439db | -15.9812 | -50.9922 | 2025-10-09 01:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 7eb4eb48-c0b5-30ac-8776-45848049bc5a | -5.4413 | -44.8335 | 2025-10-09 01:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d71449c6-3177-39bb-aa31-adf5b7c93c06 | -4.9908 | -45.1351 | 2025-10-09 01:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 89cf5554-9254-370e-a5dc-5b37f865ca1a | -18.9771 | -43.0858 | 2025-10-09 01:10:00 | GOES-19 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.5 |
| d6747d48-00a2-351f-82a3-f763cadaee35 | -4.9708 | -45.317 | 2025-10-09 01:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6cce3c36-3132-3b01-840b-0eb91cabd93e | -21.4069 | -49.1106 | 2025-10-09 01:10:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| e0624e12-e6a2-3208-84fa-e11475744664 | -18.4125 | -45.2155 | 2025-10-09 01:10:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1dd9a2f4-c703-336c-b562-bd4fb0539661 | -10.8558 | -44.6199 | 2025-10-09 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 6c3819cf-9ece-354d-b9dc-75224a35f124 | -4.278 | -48.8891 | 2025-10-09 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f71f17eb-df14-3c38-a0e4-489bda9eae79 | -7.7567 | -44.0415 | 2025-10-09 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 160.4 |
| c0646b43-51f1-338c-a088-fe1b9e61065e | -4.991 | -45.1124 | 2025-10-09 01:10:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| b6cede89-6344-34c6-8464-83c0e351d411 | -16.0008 | -50.9892 | 2025-10-09 01:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ccd9d03e-738d-3270-a472-3178bb7d87ba | -7.7755 | -44.0396 | 2025-10-09 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| e44b025d-c9fd-30ab-883d-fe8c5f53e71b | -9.1018 | -47.9575 | 2025-10-09 01:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 30d3d58f-556e-32e0-99e3-89131cc147c7 | -5.3999 | -40.9856 | 2025-10-09 01:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 942f0e6a-c621-31c4-abbd-a7b51e938de8 | -7.7569 | -44.0183 | 2025-10-09 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 92e5592f-c3bc-3df3-9bcb-f1514d8f803b | -8.521 | -46.2201 | 2025-10-09 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9bf7f454-43b6-3eaf-a12b-3365a3333824 | -16.0008 | -50.9892 | 2025-10-09 01:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 51329f1c-e526-30b1-80c6-ca4be989d720 | -13.7909 | -45.8552 | 2025-10-09 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| dd002b3a-9093-3903-b880-d795aa1cc682 | -9.0829 | -47.9594 | 2025-10-09 01:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| f816efff-d5b5-342c-8c85-de2c52176f35 | -14.4334 | -43.9635 | 2025-10-09 01:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 235.3 |
| b5b32864-737b-30f4-ae93-439be81cf751 | -8.5587 | -46.2162 | 2025-10-09 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 54269bda-3228-3965-8cbd-d2c0e2f3239b | -8.1993 | -43.3424 | 2025-10-09 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| 80615df4-2a1a-3f84-af91-f8590e1660c3 | -7.7567 | -44.0415 | 2025-10-09 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |


[Clique aqui para ver as próximas entradas](README5.md)
