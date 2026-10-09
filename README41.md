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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33e3ff0d-9c19-36f4-a00d-154019ae2fea | -3.30882 | -54.03855 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 66cf5ec7-ca01-3dc2-af52-ff381c0d6077 | -4.29979 | -60.01713 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 51aee9fb-d852-3ae6-b999-611022ec5072 | -2.56764 | -56.16494 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 04bf3415-a12c-3fff-9b59-ed311814b663 | -3.829 | -55.96982 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7fe45191-fe5f-3650-b521-145068cb1c18 | -3.17001 | -58.63339 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e573635b-ad0b-35e9-a0f2-9b757e460b3f | -2.4633 | -56.07699 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8c1bc36-fda9-39eb-8c0c-17fbde1bca58 | -3.75569 | -59.47409 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cfaa4ae9-1933-3bf2-a901-3437204fbc45 | -1.60963 | -55.15876 | 2026-10-09 00:37:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 23a8e38a-a896-395a-9730-2657dcf363a3 | -3.73805 | -59.47655 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| dbf9c486-fb1a-3e51-bde6-4a5608b63ab5 | -4.18962 | -59.40967 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5fa70e18-c84f-3050-9abf-b37c843bbd48 | -3.25021 | -54.01932 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 776cfd6b-51f9-3c19-88c0-ee012999be81 | -3.11657 | -54.1998 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3d6b69e0-39bc-33ea-b232-b44dc597bac2 | -3.50086 | -59.3041 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 439332fe-c46f-3637-a823-7ceb63663a6d | -2.49847 | -56.18069 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c8c92c42-0be0-3d6e-af99-bc1524afe7e3 | -2.50348 | -56.07758 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9f95c222-073c-3f56-8751-7aff5fe257c4 | -3.0203 | -59.16029 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6dcf218b-4f4e-36d6-b846-fc3eb63872ae | -3.43022 | -54.54524 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8a7dec7b-697e-3690-bf25-e341e4103028 | -5.25512 | -55.92092 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 73273b69-ad13-313a-ab57-622dc7a472f1 | -2.84461 | -54.14264 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5defdea5-d621-3600-9291-f73abd463078 | -3.49647 | -57.80243 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc4d9e2f-553c-320f-82a8-88fdeaa02b5e | -3.20325 | -58.01112 | 2026-10-09 00:37:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16ddcdcd-b9a8-3f72-b34a-c7b33f264d0f | -2.74253 | -57.61766 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8883aa35-61ee-31da-b101-9280975d4bce | -2.50383 | -58.08271 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9ab08e6a-9d6a-34ca-8ecf-6353c80a328f | 0.44653 | -60.54212 | 2026-10-09 00:37:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3c502c61-4c2b-32d9-95f9-fd8d3713cb9b | -2.94065 | -54.17192 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ec690392-6dff-3c9f-9f3d-3b93652a81c7 | -2.89827 | -57.21046 | 2026-10-09 00:37:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b55c2200-05ab-3a8e-abfd-676215610929 | -3.29488 | -59.40767 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 68375c4d-62ac-3fbc-bfb9-e5f05e6a104e | -1.80878 | -57.11286 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 37626fe6-80ee-334b-9a92-589a75b54caf | -2.55321 | -58.04084 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| bf4e0e00-237c-3fda-8832-e89b31a7fab6 | -1.40372 | -57.92727 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d175a2da-ed29-3883-b7ea-ecdadefe0ebc | -3.58978 | -61.63647 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 13491971-2a27-3577-b7c6-1c9df99e32e8 | -5.10016 | -56.19172 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ea116528-fc52-3de3-8a37-a7b8d3bcce1a | -3.35225 | -50.3987 | 2026-10-09 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 4f24b7bc-a801-3d4b-8b60-8faaf57f8aa2 | -3.30932 | -53.71132 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| a5b1612b-be27-3468-a301-f87bebd34955 | -1.53708 | -54.5547 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 374ebb9d-8598-3443-abd2-a3c2a3df4ab9 | -3.8208 | -59.34235 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78cf9c66-f967-397b-9ca3-dffb5a1bd1df | -3.09434 | -58.0229 | 2026-10-09 00:37:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 75e33803-cd1d-341d-917f-f0d973235712 | -3.50625 | -59.26162 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 79834d4c-9f87-3d5c-8563-0ce3f3531b1c | -3.25497 | -54.05189 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f7eea737-1886-38f9-b9dd-8c5624ed1b47 | -4.06358 | -59.83514 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fe6ff88b-a990-3b17-b225-03aeba989db3 | -3.20842 | -58.8456 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| f5fcdf4f-06f7-38b0-bee8-d05a05b98819 | -3.31886 | -61.2729 | 2026-10-09 00:37:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 85045f9d-93e0-3864-bd18-a666bb0fca5f | -2.77959 | -56.50599 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ef71cace-0b61-354a-9126-d6a9e8570ccf | -3.0064 | -54.0735 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 866ef464-f2bd-36bf-92c4-b4e202d52d4b | -2.58101 | -56.18681 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 85dee57f-b52c-3cd5-8437-6e172aeaee20 | -3.20841 | -50.84651 | 2026-10-09 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| c4729d9e-32aa-3d01-ab6a-b627a31c44b6 | -3.96474 | -59.99704 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 78e12b61-28f7-3d12-8e2e-1152ebbc5c65 | -2.47181 | -56.06362 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| eb8957e9-e961-38b4-8797-dffc16ff8af1 | -3.63724 | -60.62888 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 73afcbdc-c90d-3267-96fb-8df6c1ceadf6 | -2.50238 | -56.05928 | 2026-10-09 00:37:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b99e4cfc-387a-3e62-bdbb-41ce067ccd75 | -4.94084 | -56.87008 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3e32960f-9281-3245-98b6-683f16d73aca | -5.30419 | -60.08713 | 2026-10-09 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 94d869b9-68c9-39c3-bcf3-c93353b4786e | -3.19026 | -58.64875 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 11f3a2a7-2bd3-3b78-a195-6fc23eadc54b | -3.73506 | -57.12835 | 2026-10-09 00:37:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| abf7dd17-b105-38db-98d4-558d0c4b51ca | -3.96927 | -59.36037 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 01e8ed8c-8613-36b4-a2c5-797b69946d45 | -3.91655 | -58.89564 | 2026-10-09 00:37:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f34a3f9d-32c5-3088-856e-6fb21e217eee | -3.93142 | -56.04263 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 747f8e41-c6d6-3b37-8c0f-b025a696ed63 | -3.84407 | -55.79284 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1cfe6547-2be2-319f-865d-de86d4ace173 | -3.42661 | -60.23576 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29056af4-b238-39c9-a2b9-3cece97c3841 | -3.43277 | -56.94185 | 2026-10-09 00:37:00 | TERRA_M-M | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5aaf99ca-812a-3662-a8af-da1f129ff4e4 | -3.10833 | -53.92759 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 4514c31a-cb94-323b-8376-16742b0426da | -3.78108 | -59.24947 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f74ee746-185d-38fa-bf33-a483dbbcb144 | -4.28449 | -49.0931 | 2026-10-09 00:37:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| f4249550-9590-3e6e-9336-6db072d9ddb3 | -3.04154 | -54.15165 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 704d41e3-77bf-38d1-8b1a-ef605c90d76d | -3.51833 | -59.3494 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7dd22edc-d3c7-33fc-a9cd-368e572de795 | -3.54923 | -59.44349 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7011ff72-c112-38ba-bf72-4116c6fd5a43 | -3.56167 | -59.46859 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 068a359b-14b7-3f4b-8c6d-36bffe73292b | -3.32353 | -58.14773 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a892a1f5-0981-3a7d-9b67-246c4fed81f3 | -4.73958 | -55.68087 | 2026-10-09 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1b4ed151-b111-3560-8649-f85305435a0e | -4.57329 | -54.96591 | 2026-10-09 00:37:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 14f8cb7a-060f-3691-962e-240e7dfed264 | -3.70004 | -60.54881 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| e90223c2-e9c2-39be-b828-051fff48f8c1 | -2.99897 | -53.85096 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 07b711aa-1184-304e-8f59-131bb2717fdc | -2.83052 | -54.12811 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3e9a10a0-9bf9-30ab-a01a-70666dfef6f8 | -3.06942 | -59.17391 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d4327d71-64ff-3706-9bc7-94f43bf49708 | -1.47879 | -54.64431 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1ffc713d-eeaa-33e6-9b3f-82992220b0c4 | -1.99657 | -56.97072 | 2026-10-09 00:37:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4680355e-9170-3acc-a419-7df32a88be3b | -3.51904 | -59.22403 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f7d576c5-00fb-3bb9-bda2-d32c73faf862 | -2.49476 | -58.084 | 2026-10-09 00:37:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 04b930ea-b71d-391e-b8ea-5a6fd5de9752 | -3.57628 | -61.60751 | 2026-10-09 00:37:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b3d05078-1148-3e9b-89be-53d094fe3fba | -2.978 | -54.04391 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 7c5f3ac7-7dfe-34cd-b25d-3b064c940f79 | -3.22147 | -54.29153 | 2026-10-09 00:37:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| a6c6c330-fb79-3cdc-8471-a0110af64ec5 | -2.74138 | -54.14679 | 2026-10-09 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 99dec4ec-67ff-31ff-9e56-e4f545e1ec60 | -3.29742 | -54.01251 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| dc0a356c-174c-30eb-96f1-c8b71d3d767f | -3.57613 | -54.68219 | 2026-10-09 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e07b9bd6-9c73-3d94-8125-19c38413f02e | -3.03049 | -59.15247 | 2026-10-09 00:37:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3123afa4-dbbf-35d3-a11c-020ba37ed6f2 | -2.65965 | -59.41406 | 2026-10-09 00:37:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 452f860e-73c7-3d67-8c90-dae2491ffc1a | -3.87402 | -55.99869 | 2026-10-09 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ffd0f08-e7ce-378b-9275-2e35aaabaeb8 | -3.9253 | -55.85389 | 2026-10-09 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 811a0c56-26a0-35bb-aa7d-032beb60b00b | -3.50867 | -59.27918 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5b229cf5-16cf-37a5-bcf1-84a76447ff03 | -1.54709 | -54.5639 | 2026-10-09 00:37:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a440214a-af59-3a89-9149-08b934e83bff | -4.12403 | -59.88103 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 401de79e-6d88-32c9-9b2e-d49b904d072b | -3.52835 | -59.35694 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e05d60dc-dcd5-395b-aaf2-7ad2e40679cd | -3.25704 | -59.60704 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3fe23d15-e1c5-375f-8625-369b35c9d013 | -3.55647 | -59.49617 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 250b818e-eceb-3de3-a2eb-2673a44decfe | -3.46533 | -59.5685 | 2026-10-09 00:37:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| ec19dfe2-63eb-364d-8029-5c1fad48ebd0 | -3.63598 | -60.61967 | 2026-10-09 00:37:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 52f5de89-2149-3350-9798-38e4254fb27a | -3.11212 | -53.78797 | 2026-10-09 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c04dcb5b-6816-30ef-9f2e-0fe80c0e148f | -3.5432 | -59.39959 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 55626497-f699-3d98-ba31-0cbb5ff90880 | -3.54124 | -59.51619 | 2026-10-09 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3da56a6e-fbda-3f04-8faf-1cdfd8ce04fd | -6.08761 | -62.51889 | 2026-10-09 00:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README42.md)
