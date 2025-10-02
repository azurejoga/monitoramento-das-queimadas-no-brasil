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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87880ac9-1f4f-3038-a9be-887d5391d1b5 | -11.00825 | -46.57814 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cdec2906-298d-3616-980d-24c05d415c55 | -10.2473 | -50.32161 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 951f3e27-f223-3e54-b25e-83492a88b23d | -10.23998 | -50.33096 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe5938c6-c4db-3dd0-a894-7c602c44b77a | -7.05238 | -43.23121 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37a40817-e9a3-3e0a-b991-13a36dfa317c | -5.83621 | -45.75732 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 461ba893-7951-372c-9ec0-740bc4958514 | -8.33147 | -46.22209 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52a1a1b4-30fe-35a8-9496-4be3eea8df00 | -8.33108 | -46.22175 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3de00461-1efd-3bc3-a014-848ceb1567ad | -9.94564 | -43.72454 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1ef3ff1e-8616-38e1-b9fa-462aee891170 | -6.28042 | -44.05506 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f4c51e1-3321-3b83-9572-bf0faaa75a64 | -6.96618 | -45.33025 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4952035-34ac-3a75-aac4-b16006d66ff7 | -10.8614 | -45.41865 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11d2affc-79dd-3f43-a34e-f561f6480e49 | -11.61775 | -45.03143 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7922884e-7b80-3afa-aff9-9a75c20676a5 | -6.10539 | -43.21186 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9a294d21-c10d-34b3-b5ba-2fec4245888b | -7.78401 | -42.53064 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3a040313-e2d3-365a-a33e-989bd34f9c02 | -11.41897 | -43.49674 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 892eef40-dfe1-344e-a57c-1cceff22b393 | -11.57769 | -50.16775 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5cac20a-fb89-319d-9dc3-cbda8ad25f62 | -11.44288 | -43.89455 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69ae393c-401b-3ba9-8527-5f1a0e8bb001 | -9.48676 | -45.54764 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e7801e8-9869-3bdb-91e2-0d945833d7dc | -12.80307 | -46.90311 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10a96020-32a7-31a3-8639-f1578470ba38 | -9.79512 | -45.95004 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85f043f3-fb50-3516-9c51-e8c7abc6f83a | -11.67649 | -47.50043 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56fc4cb7-cc9f-341b-aeed-dcb45982a65e | -10.34231 | -43.74123 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af2b532d-26be-3133-9669-16bfd7de9e10 | -6.32782 | -43.04479 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20dd32b5-99f0-3383-ad98-324d1f135c51 | -8.51417 | -47.80008 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd443ed8-c8ce-3d7a-8bfe-3aedd7b82ec2 | -9.94497 | -43.66175 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ef6ef1b-1dc6-3fde-a757-d424b615ce75 | -12.01196 | -46.63906 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b18bafb1-d71a-3d40-91b8-46235c22e8c1 | -7.51802 | -44.28233 | 2025-10-02 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e5f66dd3-8842-3676-b860-3fa8eb4dedfc | -5.89318 | -43.20125 | 2025-10-02 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 325d92f1-35a1-3b33-8f66-1a772195c7a2 | -7.79584 | -42.50141 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2eeec23a-52f5-3d2f-8fe2-59f91cc33af4 | -9.32774 | -45.67318 | 2025-10-02 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9bd0fd56-e283-37a7-9a34-3fec572158e5 | -7.0278 | -38.82975 | 2025-10-02 04:02:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3ff6d90-3554-3d3b-992d-51f7a3816d13 | -11.187 | -47.19101 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 53d7558b-15b7-39ff-9486-0d92d2c4a9f5 | -9.89502 | -45.94897 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40cb403c-5e0e-3d19-a63c-da94f7cc3893 | -11.17167 | -47.27835 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 542fa6c9-249d-336f-aca0-3de2c2ae61cc | -7.06021 | -43.29652 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| abcbf778-8768-3b7d-9dd5-70c8b058f43b | -11.81443 | -47.59561 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1d93417-bfbe-3732-a51c-81a290b8b64c | -11.46721 | -45.01761 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3a833ef-de8b-37dd-8467-f2fa5011be83 | -11.48148 | -45.00099 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 554f9175-f669-33a2-90ce-e98cef5a8331 | -9.94697 | -43.71637 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8fd6f7df-7e69-33ec-8505-b2077424b9f3 | -11.65143 | -45.31088 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba65a354-650e-39ef-8452-8e98c0bcdcd9 | -7.76837 | -42.53978 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| e5c949d2-cd9a-3874-a8d3-1016666ef47b | -8.33569 | -46.22274 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87a1c1a5-2428-3e92-840f-f49d7d6ed5bb | -7.77057 | -42.54797 | 2025-10-02 04:02:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| f37db642-78d5-3d08-8372-b6ea9e326b4f | -7.55825 | -42.64398 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7df20294-99d9-3d14-b66b-146338f2c913 | -8.58325 | -49.60091 | 2025-10-02 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33cf6cf7-029d-3d26-9502-012261214613 | -11.98415 | -47.01479 | 2025-10-02 04:02:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c781d65-6389-357b-82c1-abe316f12e91 | -10.91517 | -44.31831 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5e9e223-c28d-3f22-9f21-465e03450193 | -7.78243 | -42.51867 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1903d3ae-3bb8-3acf-8306-59a44ad06a5d | -11.12318 | -47.7284 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 94b26ada-ff61-389b-81ea-0faf079f030c | -7.55763 | -42.64782 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 714b0616-99a7-336b-aea6-3b1764a9197d | -12.24438 | -44.03607 | 2025-10-02 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65c38cac-e5e2-3f7b-a8ca-10dd0ab2f26f | -6.32067 | -43.04359 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67c0d1dd-1df4-3b47-889b-282edd3d890d | -11.26694 | -47.81424 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 25bd17d0-84a0-322b-981b-db076c92a45c | -11.86103 | -44.99532 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33e77f00-0ebb-3c71-8d3a-1aec0e0def4a | -10.20981 | -50.26817 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 89285162-5b95-3e55-8855-897f1a0601c4 | -11.62077 | -45.03616 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 58521952-88fd-3dc4-bc3d-7687c287c16b | -6.70119 | -42.79965 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fa449e53-3614-36fc-bd60-d2afa587bea7 | -11.22837 | -48.21178 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 333296a3-d1ba-379a-b73d-8e7f2b3262ce | -10.17118 | -45.45972 | 2025-10-02 04:02:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 324709b2-31dd-3aec-a39c-411dee8d5884 | -9.94097 | -43.75316 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 760655b4-d75a-3e54-9d11-068e125687fe | -9.93875 | -43.74441 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b49a520e-8f80-3ff8-bd86-26a1295eb5c3 | -6.04828 | -42.4401 | 2025-10-02 04:02:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6a8c2cb-31e6-3a4f-8413-8659aaf00e77 | -11.17822 | -47.26627 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 988ef717-9710-3fd1-bd61-557c51bfe73f | -10.77604 | -46.59948 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b01bdf5f-0c0e-3617-aafe-70a3dcc3f093 | -8.53196 | -44.68468 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20ad6050-4d76-3a98-9b26-c313192bfe3b | -11.82521 | -48.0696 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0312b9b7-2fa2-32fc-8ebb-5021767f22a6 | -10.84374 | -45.39321 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 41d8e032-0e6e-307a-a021-7cb3285179d0 | -7.60585 | -45.40582 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1986a77d-759d-30b1-9fdf-d275105e90d2 | -10.70805 | -48.58158 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 618fab77-87a3-3eab-b482-2fa24d9c7361 | -9.94742 | -43.69128 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fa3a2f6-6365-3189-ad36-f6e387bbf5aa | -7.41494 | -45.19472 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a23448db-8c14-382e-ab16-09a577a90e82 | -9.94209 | -43.72394 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da7876a0-2462-3318-8f89-9ed60f059dd4 | -10.33327 | -45.2625 | 2025-10-02 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c821a57c-0fdb-3738-a40f-7fe7e9fada35 | -6.17371 | -47.26918 | 2025-10-02 04:02:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f9a76c90-5efd-3216-a203-2b46b625dac2 | -6.32674 | -43.88836 | 2025-10-02 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c24c3fcb-2877-3298-9f0a-35f5f6da5073 | -10.85703 | -46.58676 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73e10850-6fe2-3819-acaa-b395e07997d9 | -10.18532 | -45.44721 | 2025-10-02 04:02:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63a75a0e-5187-35aa-bb26-cfd277f07ff3 | -9.92962 | -43.75556 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 0219c4c3-086b-3f7c-9714-5c6086a0d074 | -9.93191 | -43.63056 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae9fff54-af07-3f00-b41b-14cc722b8428 | -13.32761 | -43.10072 | 2025-10-02 04:02:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fe04f4c4-4984-3455-bd2f-f4a4af807d56 | -11.86176 | -44.99106 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ff1c16-be99-3e48-81a7-6a3aec53961d | -9.93653 | -43.73563 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9511c63b-144d-39bf-ac20-b32040965f71 | -9.94409 | -43.71169 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1ec9a7f-19b4-30bf-95b6-c5c589ecdb2f | -10.83858 | -45.37705 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f243b586-4268-30b1-a15f-4a440a9e0062 | -5.82571 | -42.85048 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7f41690e-e466-3f87-8efb-216c7dcab4c9 | -11.46429 | -45.13255 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e84671a-5a70-3c73-88ee-930e69f35632 | -10.26209 | -50.33153 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 708d788f-5140-3554-aec0-31b90260f33e | -12.89917 | -46.90804 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f983f0f-8488-3296-8427-0dbe5e7be625 | -11.86397 | -45.00044 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0543fc42-4b20-3769-a3d2-ff96736599dd | -11.91122 | -47.887 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6535d559-a9de-3fb3-b2b9-1a84288834d8 | -10.81717 | -46.61947 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bdc1bd94-e0a4-3775-a70a-7b407ee21e74 | -9.91793 | -43.71563 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 36c2b645-7fe0-31de-9d80-57a0e3ded838 | -5.59463 | -46.24925 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fe42898-b6d8-39f1-86f4-7ccf3b312f93 | -11.1242 | -47.72923 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58e8a5ae-101b-3c17-9cb4-deede1060156 | -12.8902 | -46.93065 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 97ad8ed7-fbd9-369d-bc59-f02ddca01f15 | -10.65123 | -48.51105 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d142c22-83d3-3b0a-aa99-dbf34be28664 | -12.8951 | -46.90724 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f252688-e68c-3417-b22c-fb187016465f | -11.79256 | -47.56034 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b252db5-df6f-372f-8729-1e1174a26916 | -7.19078 | -41.69606 | 2025-10-02 04:02:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d7bc870-31a9-3ae1-a76f-1a3ecfb7b067 | -9.63015 | -46.63671 | 2025-10-02 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
