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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 322d8b13-3ae7-37fd-8f73-a9e58044c106 | -8.3803 | -46.24862 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| cb2ec460-7831-3636-ae11-bc395dfdde14 | -8.39147 | -46.24298 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8abf6373-5ee0-3623-8cd4-2567dac2bcda | -6.42898 | -44.72574 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ea0d27a-9cc4-3e7e-9a8a-eed80bfd8437 | -5.87021 | -44.8384 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2c6537e-e8ca-3f76-b0d3-d76973bce748 | -8.30699 | -43.42545 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e5595bda-01d1-37d1-8b6d-356ae1938695 | -7.45908 | -42.68212 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 307c5df3-d0f9-3dd7-9b09-c7ec20bb3db2 | -5.17846 | -42.93847 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38078431-d2f0-3e65-8a60-086a6acfb694 | -5.07955 | -40.96165 | 2025-10-17 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a66f7594-dab9-3290-9c46-2c247825f6b6 | -3.12953 | -50.21333 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2570cb60-eff6-3498-9e51-e87881719a9a | -7.28218 | -42.32223 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc9ecc61-3459-3006-bef5-7d36e868bda3 | -7.46659 | -42.65605 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0f647053-83de-31ec-bf95-630a87e87b37 | -4.50146 | -50.22601 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 083a925c-d0e5-36a6-8e96-80826cf625b1 | -8.43431 | -48.70163 | 2025-10-17 04:19:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8d122e0-ce14-36bb-a46c-00302aa0cd58 | -5.68871 | -44.88686 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e7a48bb-e7d2-3603-8cb3-1c0cd6e856d6 | -8.5549 | -44.57696 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f5390c-1c7d-3a4c-a759-cb959c99dd9d | -7.01154 | -42.00475 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7eab4a38-32d9-3b54-ac36-4b0e9dc1dcd9 | -3.37981 | -52.86938 | 2025-10-17 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d4aaef6-6a7d-34c6-8f26-18be0a80b6b3 | -11.45858 | -44.03756 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfb7996b-b61b-3a2b-be58-b769f099a215 | -10.27459 | -44.02729 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc1b22c8-1f93-3159-a28f-52d062d3e91f | -8.3807 | -46.28893 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c8ade6-6395-39b5-9bd8-23e805afad8c | -6.83335 | -42.41452 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e72c768d-6602-3efd-ba18-972005cf1d44 | -5.70569 | -45.34081 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7332882-0674-3723-83bd-dceada9fad41 | -9.0406 | -49.10003 | 2025-10-17 04:19:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ac0d48f-49df-3892-9a11-a5bbfb0438ef | -10.01474 | -45.64316 | 2025-10-17 04:19:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce1c3b98-52e7-3c49-817a-f850922ffa21 | -6.4273 | -44.71489 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbfa8fcd-3ade-39b4-a092-e53de27d4c13 | -7.85658 | -49.65161 | 2025-10-17 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51741561-f2fd-3c91-b579-4253aa55de1f | -10.43227 | -45.01719 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7b2ceec-8a85-3b0e-9f7b-9fbfdd06ea13 | -9.0695 | -48.92562 | 2025-10-17 04:19:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 875cb021-ecf2-388a-826f-969c9217dce5 | -4.42303 | -40.17374 | 2025-10-17 04:19:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe4b559a-a057-3b70-9258-d05a48e590cd | -6.6202 | -47.5646 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 836d2379-d6b8-39b9-b3bb-45a49d06a966 | -8.62773 | -45.6762 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 262485b7-17d6-3285-8d19-1e21a4e4a08d | -3.27295 | -53.2585 | 2025-10-17 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fcb98bf-4fcb-3ea3-aaee-5932b48a4759 | -6.84829 | -44.3928 | 2025-10-17 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80719b97-4208-3e83-be6e-7346fb62e77a | -8.1354 | -46.89925 | 2025-10-17 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63f42fb5-123a-31e4-910c-42d3ff908921 | -8.40742 | -46.29319 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ad2481c-a839-35fb-89c7-5adc71869720 | -5.33049 | -43.08221 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f018bf-fe38-3183-b336-5f1dae378433 | -7.32632 | -44.16286 | 2025-10-17 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbd903e6-6d82-33cf-8b55-e8a450c71b2e | -7.04644 | -45.1703 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9c00fee-ffcb-37e6-b0e7-d20f4e69a85a | -10.50783 | -43.36562 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c826744-0d1b-30ca-94e1-e2dd3a6d8e2b | -10.49747 | -43.38758 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 846f220b-8433-3537-a656-bdbccfb5453d | -11.4533 | -44.23314 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d149a65-35ef-36fd-8c0e-fed6cdba784e | -9.22041 | -46.88619 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4a8c040-4091-3883-ad22-47c4afec8df9 | -7.68056 | -44.62015 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 777d3ef9-55be-3130-8849-acfdafefc823 | -6.35479 | -41.4894 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 458a7330-188a-3e2a-80e6-1485b5cd5a98 | -6.26108 | -43.9029 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697e9e67-0ce1-3c7d-ab9a-ef009ff18127 | -8.4594 | -46.24311 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c2e19fb-c88d-3f8d-9643-ada82eec272f | -8.23053 | -44.01283 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae25b577-647a-3559-8ec1-12468ba92f30 | -8.08265 | -45.44241 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 440763e9-f77a-3e9c-bbcc-6b708c9bd0f6 | -6.42703 | -47.29853 | 2025-10-17 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd6cfba8-70f5-36f8-82c8-471a27c24ca8 | -6.35101 | -41.51414 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| caa35c52-2407-3e39-87f9-77d5e924290a | -5.87459 | -44.83202 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34bc6f50-dd7f-36b3-84f2-a1a4442efdb7 | -4.01108 | -44.17078 | 2025-10-17 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e7aa3e4-1788-3132-b70d-1d195ae47090 | -8.37396 | -46.30972 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d0248d0-f7cd-3fd1-bc0d-ce4e92082b85 | -3.4065 | -46.89988 | 2025-10-17 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c95dede-1157-37e5-a3b9-0694ba5d60a8 | -4.93275 | -41.5489 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21426e36-307c-3d93-8310-b336d462297b | -10.26509 | -44.04445 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c9529de-5028-3622-a509-96a5fca83e00 | -5.79374 | -42.49278 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 34ee2e80-5691-3317-a4ca-6ea74b06a6d9 | -11.39249 | -44.20115 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb427ace-119a-3451-93ca-cb134bad9444 | -9.28598 | -45.38708 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1630c093-1939-3d43-8fa6-b0170f3b1c1c | -4.60958 | -50.91632 | 2025-10-17 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78d24c1a-b3c1-37ba-b0c2-b887a51b335e | -10.28976 | -44.0408 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 3d159f8f-62be-3f66-b89c-ce90791bcbf8 | -6.53056 | -55.05443 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70049378-b539-3075-b199-ef5382bcb103 | -5.36715 | -43.14952 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 819bc039-a0f6-39c7-b82b-7aba356a9fce | -8.47542 | -44.18821 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 784c60bf-e2c7-3e7b-84ff-bb12b3c5a736 | -7.83305 | -44.14165 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfb856a2-fc0c-3e5b-9245-8b458dfb0000 | -8.94401 | -45.24715 | 2025-10-17 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d96ba284-271c-338b-b27e-7be4a8771721 | -3.5414 | -49.01022 | 2025-10-17 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 947bb53e-f6cd-389b-8a54-eaa48f042e9d | -5.33187 | -44.84112 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6198cda1-4fb3-3758-83ec-43c8d41196e1 | -5.06804 | -41.20805 | 2025-10-17 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fb84eb8-acd4-3df4-a829-bb4b14231553 | -5.93521 | -43.3279 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8bab02c-298c-3a84-ae9f-8fbbef7cb3f6 | -4.71764 | -46.44901 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fe394dd7-7e31-341e-af67-cc1ee51dd0b3 | -5.22138 | -45.23903 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50da6059-e1c0-3ddd-84ac-bf8ff4d9bf25 | -6.26385 | -43.90689 | 2025-10-17 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cccfc688-65b4-39da-b352-7a94bec4e14d | -6.34679 | -41.51772 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 584c4b21-0d0f-3c65-8d8a-5901f0f5a238 | -7.12728 | -46.43752 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8919ffd-5833-3711-859f-4dff9fcf08d8 | -6.74901 | -42.37162 | 2025-10-17 04:19:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b7c23da9-29fb-3f6c-aeba-9c93500dcac2 | -5.35766 | -43.1444 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f5b2809-843a-3c7d-a165-077639b01958 | -9.14282 | -46.65749 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82acc2a1-bcb5-32f7-a431-44709fcd363f | -10.83678 | -43.99672 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4b712fc-14a9-347e-8aa3-16bdb94e3a85 | -9.12951 | -46.63307 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6326d06c-3bc3-37da-847d-1b2815710e9f | -4.24747 | -48.56787 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 690bb13c-2aa1-3096-b02b-616de506dc06 | -8.23579 | -44.83203 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57f26e49-0cd4-3307-98f0-712b3e40b6fa | -5.49058 | -43.80407 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1551fb94-9799-3c7e-a495-d6e86127d1e6 | -9.27881 | -45.36816 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c5bc8bb-87da-35bc-853b-843dc07e6b29 | -5.71733 | -44.51055 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ca3df76-f4f2-359d-a2a9-2a225daf0bbd | -9.09739 | -46.68335 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0cfedca8-490c-304d-b5f3-4222ef346233 | -4.25789 | -48.56298 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c87103b3-44f0-37b2-b261-716086a112f2 | -10.10187 | -44.60145 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1620b311-7b53-37fc-a0f8-66b023143083 | -10.12387 | -44.54711 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62e5a180-b30d-3e99-8042-4b00689fe5e5 | -5.71572 | -44.52087 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bb9c68a-6daa-31df-8168-3ae94bf3c75a | -5.1498 | -46.05421 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad50ee1d-7026-37fd-9c5d-119677196133 | -7.86958 | -44.54396 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e260c60f-f1ef-3303-94d1-d90f4d10b544 | -10.26956 | -44.03773 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c902b49-6be2-3b28-9377-e4b93600876b | -7.82749 | -44.1336 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fffcbd68-519d-32ca-9ae0-0a36764b4dac | -6.6932 | -44.27665 | 2025-10-17 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 955c2389-58c9-335b-b545-2167298b7059 | -10.12017 | -44.61512 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52cf17f5-175f-3747-ba21-ec7a59a78acb | -10.57404 | -47.42319 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d3cae9d-1136-38ac-85ff-1e6018bbde85 | -8.45709 | -41.26582 | 2025-10-17 04:19:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c5524702-d5f3-3b02-bce0-30e42046631c | -5.6073 | -42.72251 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d7d0af14-9779-3a69-b741-5eba3fb544c3 | -9.05563 | -46.98646 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
