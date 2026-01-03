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
| 7a381c13-7773-3732-857e-9ba450022562 | -1.92962 | -46.42809 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9060e735-e779-397a-b52c-d03abaa97a0c | -4.42601 | -43.10684 | 2026-01-03 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5fbebe7-e518-394c-abb8-9e85e73e35ea | -5.32685 | -43.56524 | 2026-01-03 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b094cb98-bdcd-3e40-b01f-495b7eaed895 | -5.47031 | -44.70179 | 2026-01-03 04:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e4cce00-f15d-3757-9ff7-e0c6ee08c06c | -1.41829 | -46.79547 | 2026-01-03 04:08:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c0899a1-6aa4-34f6-b8b0-0d956ffcf499 | -5.5267 | -37.78342 | 2026-01-03 04:08:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b2460fe-bc59-3674-a1b8-fcc0c3c24b91 | -5.46739 | -39.27898 | 2026-01-03 04:08:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d05ed398-cd3a-36ce-b8e1-4d648413131b | -0.47869 | -48.5089 | 2026-01-03 04:08:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d7f6f18-f882-3053-b965-54a6fa2c8fb4 | -0.83432 | -48.78588 | 2026-01-03 04:08:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2b9e059-1b7b-3940-8403-5d371f9ba091 | -6.4126 | -43.46809 | 2026-01-03 04:08:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18cc6f96-793c-3d5c-80f8-fe620737f314 | -4.06479 | -43.34603 | 2026-01-03 04:08:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1fb8bfb-c84e-3a21-8fed-e02ee3cbe94e | -4.75573 | -46.71458 | 2026-01-03 04:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d59a0f38-1209-3c1b-9bb3-27ea3f55a057 | -13.42977 | -43.85242 | 2026-01-03 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e0b351c-c987-3562-841b-edc6da883c43 | -16.92112 | -40.1291 | 2026-01-03 04:10:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 98642660-942e-3f98-85c6-00b5169311cd | -13.42863 | -43.85954 | 2026-01-03 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dea2377a-12f8-31b6-bb3c-49f3f54d96ef | -13.4292 | -43.85598 | 2026-01-03 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f61e963-0323-31f0-bfb2-9f1d7fa9bcfb | -17.18899 | -40.2242 | 2026-01-03 04:10:00 | NOAA-20 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| c2161373-9e3e-3c86-8290-dba993d9d038 | -16.25154 | -42.22969 | 2026-01-03 04:10:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2d14c857-8db2-3f04-b670-e2f193cfb27d | -13.47884 | -44.01423 | 2026-01-03 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ecab1c24-dc92-3327-bb74-b03d5d7db08d | -13.46301 | -38.93593 | 2026-01-03 04:10:00 | NOAA-20 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 09983ab0-b1bc-3b5b-974e-de899cb54ca5 | -16.25097 | -42.23344 | 2026-01-03 04:10:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f8bde83-11c4-31a4-9aca-c3b3d6bfeb4a | -16.24757 | -42.23288 | 2026-01-03 04:10:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 96164649-a358-3421-8192-3c37ab2d0cf5 | -11.40675 | -40.30118 | 2026-01-03 04:10:00 | NOAA-20 | SERROLÂNDIA | BAHIA | Brasil | 2930600 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e5ba00b0-ac16-30f6-a1da-c000cc598544 | -13.47827 | -44.0178 | 2026-01-03 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f3fa0f0-17b2-3c9b-b1b2-d5c3ed441900 | -11.95676 | -41.29251 | 2026-01-03 04:10:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0916d50b-7159-364c-b04c-97487da6b95f | -9.58228 | -44.59822 | 2026-01-03 04:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a3a37a4-a280-330c-9915-f491bf5c1012 | -11.93577 | -40.53139 | 2026-01-03 04:10:00 | NOAA-20 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6cf56d58-ca9e-32c2-ab80-dacebc764498 | -13.76443 | -39.01146 | 2026-01-03 04:10:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1c4bdccb-57dd-31e0-b4b1-5fc30e35b0e5 | -13.64138 | -41.35195 | 2026-01-03 04:10:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2042ff7b-d748-3be6-ad57-d6056d63e97c | -12.21015 | -38.98107 | 2026-01-03 04:10:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 813d3dfd-427d-336f-be5e-3e50a14c68bd | -13.47552 | -44.01368 | 2026-01-03 04:10:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9f378fb-dda1-36af-b2cb-e196489e15e6 | -13.43309 | -43.85297 | 2026-01-03 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 341907a8-0be1-3bd9-b1ae-157192dd733c | -15.52189 | -43.55332 | 2026-01-03 04:10:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f412f382-3ea4-3cd6-9e32-67e9bf26d04f | -17.4985 | -41.59062 | 2026-01-03 04:12:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c4b54c75-d81c-3b3d-b106-3d6162a2e875 | -15.76678 | -52.58639 | 2026-01-03 04:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd72b4f7-e7f9-3195-91ab-1ce06271a90f | -15.76487 | -52.58654 | 2026-01-03 04:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 916ef342-12a8-336f-ab92-c200ec30f379 | -19.12871 | -40.52675 | 2026-01-03 04:12:00 | NOAA-20 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| db9a963f-bc9d-3da9-be6c-10b946b09fbe | -17.93004 | -40.07615 | 2026-01-03 04:12:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 649913db-8b1b-39c6-a6e2-b157f3ec231f | -15.76173 | -52.58533 | 2026-01-03 04:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e8b6afe-e17c-35d8-a2d8-fc9620c327f6 | -15.76112 | -52.58842 | 2026-01-03 04:12:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a404b82-51d9-3afe-b3fd-ef13898642ab | -18.4821 | -39.86155 | 2026-01-03 04:12:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 670f5d53-0d25-3a69-a579-0216a6f98961 | -28.24096 | -53.24862 | 2026-01-03 04:14:00 | NOAA-20 | SANTA BÁRBARA DO SUL | RIO GRANDE DO SUL | Brasil | 4316709 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f2fbb07-a4c8-3443-87f5-364f86e0e6b6 | 3.12824 | -60.72143 | 2026-01-03 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 088d17c1-1a99-341e-86b0-b45436915323 | 1.28156 | -60.32379 | 2026-01-03 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6cc282f3-f7a9-3f12-9e19-dfdb63c5fbe8 | 3.12779 | -60.7184 | 2026-01-03 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 143b13c4-1e1b-3dee-b8aa-571959a601db | 3.1116 | -60.97464 | 2026-01-03 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b639d6a7-0058-3404-b0aa-8ab249ff7f12 | 3.11208 | -60.97775 | 2026-01-03 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 351be5f7-4b7b-31e6-aadc-e1117403b10d | 4.34256 | -60.79551 | 2026-01-03 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d8a98c6-8b88-3e25-8b94-5c64b3969436 | -0.09 | -51.28202 | 2026-01-03 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d0a96e88-7671-3d77-9e27-c003473528d6 | -0.09057 | -51.2784 | 2026-01-03 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b3a8b87a-e1ad-3c82-9bc7-908b7bc90431 | 1.28724 | -60.32838 | 2026-01-03 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 067aa360-1dd8-3768-8d73-1b8ed0d799b3 | 2.5233 | -60.99148 | 2026-01-03 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c0090b4-c55c-3438-8007-ad391e1c3434 | 2.55654 | -60.36198 | 2026-01-03 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8af5ae6d-390c-30e0-9e48-18480bd62575 | 1.28239 | -60.32912 | 2026-01-03 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c2b00816-385b-38a8-b3c0-41af870da1fd | 3.13337 | -60.72068 | 2026-01-03 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38f49e4-faf2-341a-83a3-77afa765e69f | 1.28649 | -60.33217 | 2026-01-03 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b4bc362e-9e88-30b8-8894-e8416cda803d | 3.11285 | -60.97708 | 2026-01-03 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbdb0223-caa1-39e4-8209-657b2b182cb4 | 2.52283 | -60.98838 | 2026-01-03 04:55:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 827aa677-5e07-3086-85dd-f36eef9c0cc3 | 2.55156 | -60.36262 | 2026-01-03 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc979704-9c16-3583-8f7a-1ab086915865 | 1.28569 | -60.32682 | 2026-01-03 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 138f85f5-0975-304d-9a89-891bce2ce3ce | 4.3378 | -60.79963 | 2026-01-03 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a02569d7-7a6a-33dd-8e4f-4ea3f5ff7304 | -0.83255 | -48.78253 | 2026-01-03 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a0b30c0-7d43-3d5c-b80a-16d0093443b4 | -0.73423 | -52.42118 | 2026-01-03 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d856927-ce85-3778-bcd7-e862fd8006b3 | -3.53969 | -54.16515 | 2026-01-03 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fd30da5-728a-3d12-9506-8b5f93930a43 | -2.90365 | -54.16381 | 2026-01-03 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3363bc46-6a2f-3e22-9802-1b0840bbde6a | -4.42218 | -43.10633 | 2026-01-03 04:57:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950de4ad-3d19-30d0-a1e4-983a97387fca | -2.38866 | -56.05655 | 2026-01-03 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f2d881b-397c-3d28-9203-4a9d706e26d6 | -1.28429 | -54.55241 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 82275acd-9356-3439-8eec-f18de20f88de | -5.04622 | -43.60051 | 2026-01-03 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 781a0877-458c-30b9-835f-65cdae661ea7 | -4.42689 | -43.11587 | 2026-01-03 04:57:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baa51b5c-e8b5-3526-95be-bc2aa132af22 | -4.42813 | -43.1072 | 2026-01-03 04:57:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95859189-d55d-3f06-ae8c-5e27260532ce | -1.86008 | -54.3531 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b08afbc-a15d-3e67-9b92-1d6e90842d87 | -5.04545 | -43.60633 | 2026-01-03 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 50a7e50f-fc04-3c35-beca-11fd2229b38f | -1.26185 | -53.48191 | 2026-01-03 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5de5713b-02d9-3698-bd83-f6a5ad9cf50e | -2.21187 | -53.71592 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22c6f08d-238a-3c29-8de4-0606abcf564d | -2.42922 | -49.3184 | 2026-01-03 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae739b9-aa6e-3eba-a4d8-6cade135a526 | -5.04682 | -43.59632 | 2026-01-03 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc48e958-d8fb-37ea-b656-01cc833ebfd4 | -5.08761 | -49.50917 | 2026-01-03 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 925f8af6-c0ec-38b1-b1c3-d7e001611c26 | -0.82709 | -52.52373 | 2026-01-03 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a8e9d9e-5575-360c-bc01-12e5a0be8df9 | -3.18433 | -51.10064 | 2026-01-03 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3471ebc9-834a-314e-bb9f-24883770ff92 | -0.60553 | -52.4183 | 2026-01-03 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b29fd9dc-f635-3bf4-8e0f-42b0f2cae8a0 | -5.49188 | -45.4138 | 2026-01-03 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a274437-3a4b-36cd-a95b-8b3fdb7a833f | -4.42156 | -43.11072 | 2026-01-03 04:57:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e769a6d-3399-3946-a925-2a8f29b361e7 | -5.04602 | -43.60216 | 2026-01-03 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| aedbe441-e8b1-3190-a710-b3690076a725 | -2.94514 | -39.92458 | 2026-01-03 04:57:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e4245541-ed7a-39a4-8607-bf832acfdd9a | -1.68767 | -54.04331 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5647e7d6-315b-3735-852b-9cecbd9b3e85 | -2.94665 | -39.93119 | 2026-01-03 04:57:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b835f8a3-a1a4-3335-b6a1-69478191c1b6 | -2.08424 | -53.55477 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b3702cd-4477-311f-9682-f0cb201afbbf | -1.66974 | -53.91985 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7783120a-e7fd-343a-b64e-44d1f28f0c14 | -2.32143 | -44.79911 | 2026-01-03 04:57:00 | NOAA-21 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24ef6728-04c6-396a-bdb9-62b792547c62 | -1.70283 | -54.1418 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e43f27d5-8e63-3ea8-91a2-e6d074d01166 | -0.83071 | -48.78027 | 2026-01-03 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66d673d8-b361-302f-a22f-99f074d2c9ed | -1.96862 | -53.36106 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fd14bb9-06e7-3876-8fc5-265c2eb6443c | -5.33055 | -43.56099 | 2026-01-03 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2ce5764-a9f1-3d52-856b-bf4bb8d02d18 | -1.86063 | -54.3496 | 2026-01-03 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c6e4d6-06b1-3d47-814c-4296eafdd352 | -3.81619 | -53.72617 | 2026-01-03 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b51a46e-8ca5-3071-8ac0-b98296e32530 | -1.46571 | -53.70032 | 2026-01-03 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1244522-616a-3977-850c-a73a3054ecf2 | -4.42751 | -43.11154 | 2026-01-03 04:57:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0532d79b-a462-36ec-b4d1-427687fe4b40 | -3.8695 | -54.23138 | 2026-01-03 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f050b37-87dd-3673-83eb-2187b1a5d6ca | 0.62833 | -59.90857 | 2026-01-03 04:57:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
