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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d29f7edf-2cf4-37c8-b08f-3903fba73dea | -4.75378 | -45.78367 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de98da92-0d7b-3242-8b8d-dd7fe329ea3c | -4.5439 | -45.87562 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 4513b308-1db7-3214-a0c7-97436db1e009 | -5.93064 | -39.81799 | 2024-11-23 03:55:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a0e420a-2f00-3c34-9e0d-bf78777dba26 | -5.56285 | -46.29486 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca001a7f-f942-3138-ae9b-fbad139f9b74 | -4.61269 | -46.5064 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 33fef14e-291c-3ea7-9c13-092797248919 | -4.03046 | -46.1974 | 2024-11-23 03:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc394551-625e-35cf-a4d9-b4b4469ae7ab | -5.44572 | -45.58939 | 2024-11-23 03:55:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b962939-4776-3bae-95f1-e01b47a380c6 | -4.42243 | -44.10405 | 2024-11-23 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84f92206-8c98-36bd-9afb-58489f5fcc49 | -5.1077 | -43.16138 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0ed7af43-4d10-386c-b5fd-6603dd54ed03 | -4.61217 | -46.5095 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b2f4a803-0f69-3db7-9353-218694dfff3e | -4.44713 | -46.34651 | 2024-11-23 03:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8daeb6f4-d5c7-3815-8aaf-a9a134b9be50 | -6.41908 | -39.5787 | 2024-11-23 03:55:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4f407e6b-efb7-3459-ae18-682a09492cb4 | -3.80656 | -51.33757 | 2024-11-23 03:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4bfc608a-cb8c-3599-aa21-4ced470a5dd9 | -7.02023 | -39.22158 | 2024-11-23 03:55:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 05ac0fc7-c9d7-3461-98fe-d054154e5fee | -3.68419 | -50.12061 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2fd3888b-d333-3a8c-a19a-613145d123c2 | -3.706 | -47.61512 | 2024-11-23 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1223c137-6853-317c-97c8-4764b0611ae8 | -5.92576 | -39.89243 | 2024-11-23 03:55:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 154ebc0b-f72d-3ca6-9864-650ec0e039de | -3.68035 | -50.11879 | 2024-11-23 03:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 30dd1ba5-faa2-3212-8be4-827ada0e6c84 | -4.10082 | -47.81191 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97090227-2a97-3dea-a9f3-c40436eaa18d | -4.10325 | -47.80727 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ebaea25-554c-3381-bd4a-b49099b164d0 | -5.75353 | -46.26348 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2fc7a154-de70-396d-8bb0-92d185f64987 | -4.69101 | -45.85504 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7bf8748b-a073-3ecf-a21b-4620f8e8834f | -5.75449 | -46.25777 | 2024-11-23 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a051e384-53ed-3c6a-8c62-00842dbd3fe3 | -13.29241 | -39.80725 | 2024-11-23 03:55:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 16d3b87a-68d0-33ab-a405-f3b501dd5b67 | -4.34628 | -46.01439 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54f41649-c08b-30ad-9d35-8c26af53a3d7 | -6.13284 | -44.72802 | 2024-11-23 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 109ee45a-0403-3149-a576-08e21436bd57 | -3.97028 | -46.649 | 2024-11-23 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 90fb1751-a75f-3b76-9006-15a36cfdbab5 | -5.16028 | -47.04228 | 2024-11-23 03:55:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dc83283-24ec-329a-9c4d-32c9805d3523 | -5.23261 | -45.11094 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef605f63-ec65-3569-b175-58414cb11308 | -3.95051 | -47.96746 | 2024-11-23 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24f934a7-b86b-3405-97a8-30f43dfae3cb | -4.60898 | -46.49669 | 2024-11-23 03:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 1acffd00-9690-3dd4-ba4c-6c6db512733f | -4.52528 | -42.91467 | 2024-11-23 03:55:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 564c243d-dba7-3699-8e0b-6b0ac66bb81f | -4.54785 | -45.88246 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d6590afb-8312-35c5-b07d-a4edc770d193 | -4.72261 | -45.49109 | 2024-11-23 03:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ee3c6f8-ca11-3796-be78-99950d734299 | -5.93078 | -44.72926 | 2024-11-23 03:55:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e06fb56-1d13-3542-86dc-cb52b539f4e6 | -5.58803 | -45.20374 | 2024-11-23 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb33cd7a-b048-3a70-ad43-e4ee8872edc4 | -4.21962 | -46.16119 | 2024-11-23 03:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64082d16-6275-373f-83c1-90df8eee6f86 | -21.3881 | -48.59911 | 2024-11-23 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6db75920-d359-30d2-b90a-395adfa70d48 | -20.99689 | -51.79387 | 2024-11-23 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b8f3cb74-be48-3045-b972-6bb80ac320ea | -23.59342 | -47.43776 | 2024-11-23 03:57:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5f0adad4-5833-38f7-b8c1-17335736f748 | -20.76376 | -46.76956 | 2024-11-23 03:57:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d8cd3165-2f49-3c72-a599-978ec08465fe | -23.9835 | -48.91698 | 2024-11-23 03:57:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c98ef172-5e33-3a49-b548-4306659ce5a6 | -22.06487 | -46.91433 | 2024-11-23 03:57:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a77d021-4316-3d3f-8710-4607e3544a94 | -24.11968 | -51.06207 | 2024-11-23 03:57:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bb6ae8e7-89c5-3621-8800-03e7bc61a49f | -23.98569 | -48.91938 | 2024-11-23 03:57:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4f1b855-0d09-332c-9765-eb8a93388ac2 | -23.63029 | -46.42679 | 2024-11-23 03:57:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 665d2377-56ee-3c77-8c67-3ff675dc9b91 | -23.98141 | -48.9184 | 2024-11-23 03:57:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b59271e-81bf-385c-95cc-fcb17b3f7f9c | -1.7359 | -52.7181 | 2024-11-23 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 524b9b9b-1ed4-3443-a232-2f495040cec9 | -1.2596 | -51.762 | 2024-11-23 04:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 36777954-6143-3068-a4b6-4183f5472f65 | -1.7359 | -52.7385 | 2024-11-23 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1f3816b5-e5e0-3b9f-8d98-713ea61b3c91 | -3.5159 | -53.8132 | 2024-11-23 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 5a5850c5-13ad-34bf-bce4-306a71370711 | -2.4456 | -49.0816 | 2024-11-23 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 40535da8-9bf4-3651-be5a-4969a85ccdb0 | -3.2768 | -53.8199 | 2024-11-23 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| dd21be26-b3a6-39c4-9bcb-9ebae8fdf0e0 | -4.6085 | -46.5002 | 2024-11-23 04:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 0c435680-6966-3448-abaa-5afd40d840d8 | -4.2605 | -48.697 | 2024-11-23 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a980b15c-2b02-3139-b383-1bda82c09ada | -4.5216 | -42.9078 | 2024-11-23 04:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8c92af0b-aed9-34ac-9ff9-7273dd728bc6 | -4.5403 | -42.9066 | 2024-11-23 04:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 2799bc75-9d73-303a-878d-62ebb09bb8ca | -1.7359 | -52.7385 | 2024-11-23 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d68f7b75-e023-39cc-be19-eebf43e16643 | -3.5159 | -53.8132 | 2024-11-23 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9c525420-591e-30a4-865f-94440f56c732 | -2.4456 | -49.0816 | 2024-11-23 04:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 19df6896-d15b-34b5-b204-79f92f0f4f95 | -4.5403 | -42.9066 | 2024-11-23 04:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3d9f8ef8-d18d-3858-b749-c9f9f083be66 | -2.8166 | -54.0326 | 2024-11-23 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 75242d17-a630-3a89-96cf-1342e850e4c6 | -1.7359 | -52.7181 | 2024-11-23 04:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| edff9724-0bcd-3dfd-88f8-dc6b4eb0e8df | -3.2768 | -53.8199 | 2024-11-23 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c1d412d0-bf65-308b-b340-829d7a1731b7 | -4.2605 | -48.697 | 2024-11-23 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 8b91dfdb-d654-37cb-b9ff-e0e08036d5d3 | -1.1103 | -53.3953 | 2024-11-23 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 57587e0b-f52e-3ee0-addc-d2dbe7b2b659 | -4.6085 | -46.5002 | 2024-11-23 04:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 113.7 |
| c533bd82-1b16-3f7c-94bd-5acd49e184b9 | -2.65597 | -46.57141 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae7f48c9-f52e-3208-b4ac-481951f7d289 | -2.71294 | -46.09729 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25b8ab80-0e7f-3a4e-bd82-7a9cb751f91f | -3.07596 | -45.9746 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ab80c3-0d9c-397d-88ee-de704dcec028 | -2.6812 | -46.16272 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5dc3a21-42b7-3ee4-8058-7b6cacfb58e1 | -0.91767 | -53.10416 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd27594c-eaf5-3849-8b22-78dce9544501 | -1.60447 | -52.58229 | 2024-11-23 04:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 645ea50a-8fe8-37c9-a456-07181f069951 | -2.43032 | -49.37482 | 2024-11-23 04:16:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f266c4db-eecc-308e-9fe1-4602bd55c77c | -2.64826 | -46.57428 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4948e45-6598-3c82-97d8-763462a72b56 | -2.55233 | -46.53928 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a4ada58-2058-34c7-b114-b45304ae7ca7 | -2.55691 | -46.5563 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5af85d98-0764-3cfa-a18c-8343e2d5c73e | -2.42278 | -46.5116 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb3d12fc-6e24-385c-b482-bff8b28c9baa | -2.22623 | -50.51636 | 2024-11-23 04:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c81f5193-cc23-31a2-9e6f-6da4f6e42c1c | -1.2061 | -51.75534 | 2024-11-23 04:16:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0228c34-0e4c-3f44-9651-e3078e8d3679 | -1.6181 | -53.31294 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbbfacf6-5e29-3601-b92a-9561edc423de | -2.39801 | -48.60866 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891e98fd-e5c8-39c7-a49b-c6b788974d22 | -2.39746 | -48.61211 | 2024-11-23 04:16:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50d745e0-5c2e-325b-86a7-3e15b48fd958 | -2.69954 | -46.27229 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c95f99da-8995-320a-aeae-6d5a06d787ff | -3.0794 | -45.97513 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| acbc0e8a-e7d6-3ca3-b9b0-a727d4657e5a | -2.4415 | -46.53095 | 2024-11-23 04:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cdf6cfa-e943-36bc-b91f-1a9b3ba0223b | -2.40716 | -48.327 | 2024-11-23 04:16:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25794ba0-aa03-3b52-a14b-cbf7cef1e801 | -2.64964 | -46.2485 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73d24e31-2f8e-3a80-8d3f-20c9003f7e6e | -2.27498 | -47.37034 | 2024-11-23 04:16:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| defd699a-27eb-3525-a57d-656e1690d933 | -2.41492 | -46.0322 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 504a57fb-7758-3412-a25b-d7dba40bec41 | -2.64677 | -46.24406 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f28d679d-f0be-381f-8c1c-d56f761eb3d3 | -2.55462 | -46.54778 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7455aec-cad2-3b7b-b46a-c2f7dbbb3aa7 | -3.29576 | -45.69408 | 2024-11-23 04:16:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9590710b-377d-3777-a525-9088c8b75017 | -2.66442 | -46.15617 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e01e7a57-4327-39cb-b927-32142d5b12b7 | -2.57045 | -46.56257 | 2024-11-23 04:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94afe56-9aae-3bf3-8e6a-e8f0f5d1a577 | -2.656 | -46.25346 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3ef05ef-16b0-3d20-b1dc-3993a00fe472 | -1.18333 | -51.9586 | 2024-11-23 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7c0bc11-4aaa-35b8-a953-1f90acf36730 | -1.46221 | -51.12106 | 2024-11-23 04:16:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70eb9a9a-6216-37d0-9eb8-ff277606afa8 | -2.89498 | -48.02285 | 2024-11-23 04:16:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c2f259a-e698-39b4-8ae4-0a81acec0940 | -2.65313 | -46.24905 | 2024-11-23 04:16:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README28.md)
