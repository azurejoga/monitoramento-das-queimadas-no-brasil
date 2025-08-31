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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58784a03-1e71-3c6f-8780-d94556f1e1a2 | -10.60226 | -44.32818 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d095104d-e056-3816-973f-10d0d496d935 | -13.34367 | -46.98618 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8db5f2f6-bcac-3e5d-935f-6b0f7a0135d5 | -8.67525 | -62.43035 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99ab4bb1-ee44-3aef-bd18-5660098513ea | -11.28109 | -63.24302 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b082586-e89f-31e6-b093-d0a705c3ee95 | -11.88943 | -46.42451 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8f5f2e2-31dd-3539-a703-1b7f7d0a112a | -10.3115 | -59.2037 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 558d8f97-f3d0-3ccd-87c3-1a39008a1ca3 | -8.74215 | -62.39445 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fa1b667-61fd-318a-a0b5-07883242f635 | -8.56226 | -63.01442 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05a629f7-b634-3421-96e1-0fa44d6111c0 | -11.81491 | -46.44153 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dfd331a3-d2b0-3b00-a68f-47108bb60faf | -15.94189 | -41.40726 | 2025-08-31 04:51:00 | NOAA-20 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 521a5fb2-f52b-3ee7-8b2a-1f30065a428e | -13.03015 | -56.91065 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0877bec-0e2c-3ae0-9b0b-cb44d2d52430 | -11.07567 | -44.74535 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7629d51d-e6e8-3e5f-9961-7fba8ddec187 | -13.35699 | -51.74849 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feb65013-3e10-30bc-b2f4-c93e1637dc09 | -13.36704 | -54.38316 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd52918c-c4b6-3aa0-9e80-3ecee125fbb5 | -13.36648 | -54.3867 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b91ef5-eb02-3a41-9ab9-b74384419714 | -9.46882 | -47.60736 | 2025-08-31 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6222d7de-ee22-3dd9-a941-271f40645e6e | -13.36036 | -46.9467 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 199188c8-47e8-3bcf-a8e2-a50847aab870 | -13.6843 | -46.89282 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9827c668-faa7-3905-8107-392c13ad281f | -11.82151 | -46.53998 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 341bf6e7-1179-3eb8-ad72-4af4e3a78abb | -15.07515 | -48.62404 | 2025-08-31 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6d80b3b-45c9-3354-a34c-ddaa3b17f7ad | -14.36192 | -53.33233 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b2ff74e-c75f-3502-80e4-15c62f463d88 | -13.35726 | -46.95323 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eac1407a-13d3-3c1e-8e63-da5f34ea8406 | -9.45084 | -62.35476 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0741d74d-a8dd-36d5-bad3-43e4dfdbc1c2 | -14.62658 | -48.05657 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d9cbc1d-f109-320a-a4c8-fdd7b8de9e99 | -12.92641 | -56.98973 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f86bc6eb-9216-3147-b76e-9c676e4d6443 | -8.34474 | -62.93111 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a71a7ce3-51d8-3979-90db-61424993518f | -10.59491 | -54.90986 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c96b32ca-01b1-3cc1-bf0e-9f9102a9f84e | -7.95393 | -46.41474 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba65e634-e035-3be6-91fe-16732a384301 | -9.44455 | -62.33028 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98e48dd5-0eae-36da-93b5-4b23fb608b4c | -14.61638 | -48.06744 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7fad810b-7493-38dc-8e1c-0f9174d465b7 | -11.83004 | -46.42626 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| bd13b202-b25f-3176-b46b-51d419b01120 | -14.99128 | -46.71312 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3419c51-0e1f-35d8-bdb2-c6ddf7488566 | -8.95298 | -50.00015 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca871f1a-1e1c-3e20-b227-f8a559635714 | -13.364 | -51.74945 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e5b769c-c150-3192-bdb4-a054f4c66366 | -13.2604 | -51.98368 | 2025-08-31 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae22f30f-8933-3234-8b87-5a5ea0766222 | -14.13677 | -47.05955 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 978e8daa-8dad-39cb-9d36-4e285854f304 | -7.71325 | -50.27766 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6802e914-e46f-325e-9fa6-2efde8cec5c3 | -9.43755 | -62.33894 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e63a836-e594-3430-916c-8e6f66026999 | -8.73576 | -62.38985 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 474dabf5-9a90-3448-b10e-34cdc0ddad17 | -7.95882 | -46.42566 | 2025-08-31 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8bb0b80-4576-33c9-ba6e-ed0acd4e5be5 | -12.31628 | -45.73056 | 2025-08-31 04:51:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| efea416d-2ea8-350b-83d3-f7aa8356bcac | -8.73922 | -62.40072 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4beb11fc-d17a-3713-a626-4c98e21029b7 | -10.99785 | -46.94228 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 960e8a77-c023-37d4-b88f-5bc24add44c5 | -7.74059 | -50.26415 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7155b96e-0262-3a85-a84f-08f72fa68e7f | -11.84045 | -46.43024 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 505227ca-56a0-3eff-84c8-c9c7bdf2a149 | -10.12733 | -58.0225 | 2025-08-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27314246-f723-32d0-8626-f3a2e1f9d4be | -10.93785 | -46.84024 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f6dc7d9-4e1e-3820-9d86-3cffbc9156d5 | -10.75712 | -59.82589 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adb6ec6e-1a3f-3062-b6be-577d70b9e9c2 | -14.9984 | -46.70771 | 2025-08-31 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 855ca8ca-ab1d-313e-bffb-59cb69e3070f | -8.83905 | -47.48688 | 2025-08-31 04:51:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c43fd148-6d9d-31b2-985a-283c82db3d7c | -10.66613 | -46.26763 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ce3c78c-b3b6-3812-ab6e-dca3d7e5fd7f | -13.50346 | -46.83255 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5639f78b-959e-3a1b-bcb7-a4a18c0a2347 | -13.26386 | -51.98424 | 2025-08-31 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ae3fdd5-07d3-3f95-97d9-391ce35ebd22 | -11.82439 | -46.4427 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c83a5ff-dc5b-3298-9a31-e33a2e670e75 | -8.65911 | -62.82893 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 423a464a-445f-321a-831c-3f8a91d8b1d0 | -14.63502 | -48.06073 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0c24558e-a1a2-3aa0-81cd-2a1734311362 | -9.44442 | -62.3603 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64205b83-a4b3-3d1c-86ab-12d39d8dcef7 | -13.39517 | -46.84088 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f645718c-5162-3c92-a3de-12094516efe4 | -12.93349 | -56.99095 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cac1e9ab-78f9-33fb-a8f9-6a92ca732b09 | -10.3212 | -59.19745 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32b7198a-f743-32c1-be28-8435d3747ee7 | -11.56003 | -47.61287 | 2025-08-31 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14e05256-b937-34ca-9672-c22faf6a59dc | -13.35898 | -46.95713 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe6a9054-4412-33cf-a622-aedc587af634 | -13.48728 | -46.96144 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fa1f8b73-1497-377e-bb41-4ae8b9eb3109 | -10.87918 | -55.76474 | 2025-08-31 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e1489cc-6134-3f07-9cf3-25118e0906fb | -9.4432 | -60.57674 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a94dc720-1b33-3344-a568-75c5075dceae | -15.67243 | -43.23099 | 2025-08-31 04:51:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 93412618-8488-3ad2-9b0f-3a5004b5485b | -8.7829 | -46.59073 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5bd23cf-51f5-3e32-92d9-55f85d2bf177 | -11.34597 | -43.64062 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7a9d0970-6555-3c8e-b30b-d280587db544 | -10.66752 | -46.26961 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22cd5252-4f15-32ae-a73e-2ca6670ecdf5 | -7.71877 | -50.26514 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6b3f2e6-237e-3488-a4a5-acc74ce86d92 | -11.83103 | -46.42849 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d2614564-9b69-365d-9d94-3d1540a9839b | -12.09728 | -44.72795 | 2025-08-31 04:51:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 64ad683a-6efe-3f61-852f-b869e179e0bb | -13.02364 | -56.88459 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9335cc59-75b9-3f88-8059-4841fe2cb8c4 | -8.73921 | -62.38024 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6faad1b3-64a0-38c0-9187-347601118502 | -8.65795 | -62.83301 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8790225-073d-351e-91d7-20365d2207e3 | -13.4744 | -46.96652 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23cbd8ce-d6be-3d4a-b6da-35e8559eb643 | -11.8827 | -46.71215 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8c94435-5171-3422-9e6b-d6c76c05ecfb | -11.36235 | -43.55354 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c3c20f2-a8b2-3d30-8308-4350acdcfe5e | -12.80362 | -48.09822 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a094dd33-6ca5-3689-b933-d62787de5a81 | -9.44905 | -62.36449 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 482179a4-7edc-30a5-9e53-b640b2fee188 | -9.455 | -62.33216 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3dc54fa-1559-3d9a-8893-8899fbd33815 | -11.82471 | -46.51508 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32dad8aa-9999-360b-999c-70265ccc46da | -8.78506 | -46.5941 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8ee4103-6b63-32c7-91aa-3e2e228ce234 | -11.00234 | -46.94308 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a05c160-1e11-3ab2-b9f6-26dc7ff55e4c | -14.6305 | -48.06102 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6df5e59f-6175-3152-b037-656ae64944fd | -8.74745 | -62.39544 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b29441e1-e9c1-3c5f-b8ee-5ff1e7d02a0d | -8.29503 | -46.31226 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97ee1f63-4fa3-3ef2-9585-83fbe98d139e | -13.35573 | -46.94576 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45732c5c-76fc-37f7-b587-b604c7eb8089 | -10.67016 | -46.27317 | 2025-08-31 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e86b1283-eade-3a88-a028-dcb7c2f419ce | -12.41011 | -46.46675 | 2025-08-31 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e4f1f66-f671-374a-92b0-a3bc982eb25b | -11.06818 | -52.04707 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5470ce3-6e72-3d6b-a5e6-31bfa54e9f4f | -13.46803 | -46.97871 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dfc35d06-ec72-3a4f-bb0a-7d2a0a597411 | -9.30412 | -59.22219 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a60e9e41-5842-33fc-b624-ab91ebd1742e | -7.71448 | -50.26965 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3968abc5-9b6e-3b55-ba83-7c7d945ac00c | -10.42168 | -50.86454 | 2025-08-31 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7a23458-9afe-33e6-b321-c3be16d04922 | -8.73862 | -62.38353 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d438accf-aded-336c-a1a3-ee4421c92039 | -11.82503 | -46.43767 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07025810-3a76-39ee-be1b-14cf0317bd63 | -13.46969 | -46.96613 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45c45423-af8c-32ab-be11-22cdf9572e6f | -8.68712 | -62.42563 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cecd53da-3ee6-303c-92c4-1630173aeee3 | -8.65184 | -62.83558 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README67.md)
