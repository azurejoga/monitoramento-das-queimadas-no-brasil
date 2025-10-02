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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 447c5913-ba65-38e9-82b5-6ebf94a96cc0 | -6.48998 | -44.29037 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44c0c27e-4ab2-379c-b692-545bb26cf428 | -12.8343 | -46.87 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 638cce07-d82a-3ba3-bbc3-7ae83182ccd8 | -11.00012 | -46.5999 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 0fc85c44-816e-3501-a54c-fcf5087a81e3 | -10.22638 | -50.28563 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 934fb39c-7ea2-3f0d-947c-2c301077c4b8 | -10.3309 | -48.18257 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 151f5808-cc96-3b11-b011-500d07a5d868 | -10.82829 | -46.62926 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 165b9de6-a74a-3c33-b036-c902dd50188d | -13.01048 | -45.2201 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44a2a5e4-e377-3eaf-b7a2-bdb6d5a44c14 | -11.8132 | -45.01677 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31ea2405-a42f-3893-833b-274ccb78257a | -9.93212 | -43.71803 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| db845b2b-d000-3a83-8f1e-aa4d6ca7c0d7 | -6.80023 | -45.96845 | 2025-10-02 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7873809-f518-30ed-a49b-fd366644a2d6 | -6.69864 | -42.81555 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| fbb80475-a8d1-363a-9fd6-2e0e6fe87d9a | -8.92396 | -46.06884 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61fe4d07-1971-34b8-918a-5a1f9ed716ae | -8.89225 | -46.60271 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75b9c0ca-1be8-3e34-aaf5-9d947505a0fe | -11.00625 | -46.58939 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b819658-c1fe-382c-b2b2-a185de38bcd6 | -7.00557 | -44.50786 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c919af2e-e2bf-398a-8515-7c29edfe8072 | -11.44134 | -43.8819 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eb6cacc-8040-307e-b09f-c723eec996a7 | -9.89843 | -45.95335 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad8b4f38-2fc3-3c9d-8705-9760e00484dc | -10.21994 | -50.3487 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 588710dd-f741-3915-b44b-3b443883433b | -10.83031 | -46.61771 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9497e566-d1ae-3690-9cde-7e63c0729dfc | -8.78843 | -44.79896 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aba4ba3c-a5dc-3c84-8973-1116cb4915bc | -12.31312 | -46.87945 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31976e3d-0ee9-39a0-a37e-159e5f0923ff | -5.83353 | -45.77317 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dcbd5de-5e92-3f71-bcac-967e36bd4cca | -7.05685 | -43.31728 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 79be8909-81d9-36e6-b392-11e29e7e8f89 | -7.77872 | -42.54143 | 2025-10-02 04:02:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 7d5f5373-d98a-3fd5-a966-a4fadc3b406d | -6.4664 | -44.20123 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca392f0c-bb23-3ae3-a7dd-c8478bbac007 | -9.94543 | -43.70351 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c391704-4396-354e-99c8-0877d9d101b8 | -6.82185 | -47.9749 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0945d61e-dc96-3059-a664-228330c18a3b | -7.78304 | -42.51487 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 00fddee2-2862-3f06-a1bc-abb6032bf65e | -11.82917 | -45.00345 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 197fb9fe-9098-3cb7-8f39-1c78d9c4b484 | -10.65214 | -48.50591 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ed20fbd-80d4-3cac-a6e8-5508f30bb7bb | -8.55814 | -44.64505 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7fbc4031-0e1c-3759-8cbb-a7fa75f1afd1 | -7.77182 | -42.54033 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 30665725-16eb-3e7b-a72f-6e2029a6cda5 | -11.3604 | -44.93629 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cba77dab-896b-344d-8a25-b851d26d3a12 | -11.13095 | -43.38969 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| bab020b8-7881-36e1-8784-7954ae5747f2 | -9.41867 | -47.35638 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4069338c-a58e-362b-8dcb-c4b2bfc9d7ac | -7.0171 | -44.50985 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7bd6b209-b5ac-3256-9c16-8b818e161596 | -9.03434 | -46.68123 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 988c52a6-0859-3e5c-b75b-2194521b4665 | -12.11614 | -43.42968 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86bf4290-94b9-3d2e-bbfe-ffafb763335f | -6.24357 | -45.32568 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b288969-008d-37e1-8613-e3cbc35e1472 | -10.82248 | -47.97074 | 2025-10-02 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f1ef3533-6ca1-3eb3-9e72-e9c205e49bcf | -11.73609 | -44.42365 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 379c9246-6e61-32c9-9a67-83276ddc4a71 | -11.48298 | -44.99196 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 41a0ab66-c092-3f88-b9ef-7cba5c34aad7 | -8.55537 | -44.73209 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46417448-98d2-30e2-b290-0f1f6398d548 | -12.88362 | -46.92474 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcb0ee2b-96f1-3b26-997f-712072096def | -7.15756 | -44.99218 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a764b77-f129-31de-9f95-645d807be653 | -9.94255 | -43.69883 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 869400e1-da94-303c-a425-1e6b4b6b8d74 | -9.93385 | -43.75202 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 23d65b0d-c6cd-3732-abd1-cfa37e98c781 | -7.79867 | -42.50574 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e034c122-7460-3ac5-9c27-610980fa3f62 | -10.22546 | -48.21845 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81c11b8b-36bf-31e5-8629-65abb808f8a3 | -12.75597 | -46.91093 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51e397ca-024b-360b-abf3-ded8f9b816ac | -5.7936 | -44.91383 | 2025-10-02 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3db075e2-4bde-39c4-8cd8-aec3e1f71356 | -11.80964 | -44.90159 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7767fbf9-3e29-3794-9dba-371d9d6be616 | -5.78831 | -44.69865 | 2025-10-02 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b8ce8eae-6e71-348d-a4c6-94e4ce6b173f | -6.96047 | -45.31427 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6ec56b96-4cbe-3ad9-8c35-5fc5bfa73dbe | -7.15445 | -46.06006 | 2025-10-02 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41625af7-0fbc-394e-888e-afe7ff0aa2f9 | -9.94252 | -43.76606 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 06ffda84-76db-3547-8594-3c34ff4d9294 | -7.01629 | -44.51466 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 98220799-3c4b-3859-a63c-4e6a9b9bb513 | -11.84061 | -44.9591 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd8850b9-4383-3300-a319-23f949273814 | -8.50517 | -44.7042 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4337000-d484-323e-b487-288dda19a8c0 | -7.55256 | -42.63518 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1cfc58a3-e6a5-328c-b272-2323f9e590c3 | -9.93479 | -43.7017 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7116eba9-0ee2-3ab3-b7fb-c1434c69a46d | -6.17456 | -47.26414 | 2025-10-02 04:02:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fcf17991-05d5-3d74-a0ec-a2fcbe43d04e | -11.80034 | -47.57444 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21016285-5c8a-3f39-b7da-040ca2197916 | -11.61401 | -45.03092 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a0f3f63-075d-3944-9652-1e760739653c | -6.33272 | -43.03717 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2320395-2465-3069-8994-0c34eae7997b | -10.83097 | -46.6139 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3254a251-95bd-3792-8c4c-2b44c1515ea7 | -10.21654 | -50.33731 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d66e7a12-f1ad-3cce-94b9-dab1bed05189 | -10.82964 | -46.62154 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 970a8c99-00bc-3f57-ad66-10d4a41ab6e4 | -8.51228 | -44.66227 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aaa1a04-6322-3485-89ae-0e9644c1030f | -13.00757 | -45.21498 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e239cc0-300b-3b30-9732-5cffb4c45d89 | -10.24535 | -50.33197 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0d4f662-eab4-373e-870e-0e53ad49a8b5 | -11.1549 | -47.19769 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f082667-b0c6-3bc6-b250-30200ff82615 | -12.84196 | -46.94548 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 484e07d6-b6f9-3ed9-be58-9996aeb534d8 | -10.246 | -50.32851 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4aae35dc-e0dd-334c-8c9e-99cd65c4e030 | -7.55821 | -42.4052 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50c2eba9-535e-3c70-8d62-1e55f316f6c0 | -7.31015 | -42.87376 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2f9a59f-4e89-34e0-a450-f8e7c9e321a9 | -12.87803 | -47.02079 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa0b2a13-b632-3f6e-be2a-2b2479da46d3 | -11.67435 | -47.48733 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 174b4c48-bde1-33ba-a731-e0c526678ca4 | -10.26467 | -50.31772 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c21b8aae-078b-3ac8-917b-538c986db946 | -7.7285 | -46.21172 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46a25196-993b-3328-8362-d9bd2b6662fd | -10.25396 | -50.31571 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 175f89a5-caa7-3a92-b8db-4031d616d7a2 | -10.24323 | -50.31371 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a68c8dbf-7dc7-3d3f-99db-175e6a3fe3d5 | -8.20998 | -43.59265 | 2025-10-02 04:02:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cff15ba-a238-3753-bff6-df80e9ab4e91 | -6.16966 | -44.58653 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9b9852dc-6c37-3a1a-849d-0080a6c85e9b | -10.24454 | -50.30683 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7d8a157-60c2-313f-868c-19ba7286aad7 | -6.04928 | -42.67849 | 2025-10-02 04:02:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0636a8ce-25e2-355f-aa13-07016ba801bf | -9.95518 | -48.78216 | 2025-10-02 04:02:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f8128bd9-b006-3f3a-bb76-53ce3349ecd6 | -12.89795 | -46.91501 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acb7eea8-0303-3649-90c0-b3e1cfdee3a1 | -8.64216 | -43.98071 | 2025-10-02 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7e71487-1a8e-3351-964a-75fb7697ae0e | -11.83943 | -45.01029 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fcff4a12-8fe3-3c63-b51e-b85d95c1efc9 | -11.95074 | -47.10638 | 2025-10-02 04:02:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9226e3e-d4fb-35b9-933c-8403989659cf | -11.8647 | -44.99614 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9fa334df-f42e-3672-a9c7-9e3f41f2d620 | -7.7712 | -42.54414 | 2025-10-02 04:02:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| de24f25b-c85e-3033-bd4f-fbade1b736ca | -9.94851 | -43.66235 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3812c9d5-c409-34c8-8185-0f1a0e86fd1f | -11.27062 | -47.81939 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a3198235-82ae-3cbc-8708-0a4a021e8239 | -6.49069 | -44.29307 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b3bde46d-18cf-3c7e-9da1-4deed6bff275 | -10.83244 | -46.63 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9d297b91-06bf-39b3-a476-95730915b5cd | -11.82101 | -45.00661 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e08feb73-06ac-3c0e-820d-2cf51b23fb55 | -10.99672 | -46.61897 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f0c2492-641b-3275-a11e-4bd1b1d2bd21 | -11.812 | -45.01455 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
