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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52a09aaf-ccc5-3217-a9b7-bb12a8bf1494 | -9.7759 | -47.17564 | 2025-09-21 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bc5e5cf-a30b-33ae-b7f7-65b156737035 | -3.60126 | -47.51675 | 2025-09-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01dc8f63-0eb9-3639-82e2-65695380ff40 | -7.47493 | -44.37995 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc64c53-464f-3090-b17f-d02370dfb279 | -6.01281 | -44.33157 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c389cb1-0d1c-3c76-9470-8a2204f3d0b5 | -5.01355 | -45.2066 | 2025-09-21 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28aeaac6-c612-3102-9b5e-650a8d00b8f3 | -4.70905 | -46.47282 | 2025-09-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b4aa6db-5dbc-3d66-a2f7-3edbee744965 | -7.93297 | -44.10938 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff5b5924-25fd-3b54-b86e-fe5bae3b1001 | -9.42572 | -44.71647 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7185255f-7238-3f01-9ef1-d0290d38731c | -6.25134 | -43.75169 | 2025-09-21 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d134de-e328-3010-bca8-0ae2dfb5999f | -7.9348 | -44.09809 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| caa43a36-2bfa-316b-a18c-15f0c85d4c2a | -11.4893 | -43.56799 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5dc48111-c8a1-3e2e-ae43-488c28e0224a | -6.31828 | -42.36936 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b6150e0e-6c38-3468-a194-98fca79b18ce | -4.60488 | -40.7308 | 2025-09-21 04:08:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1c6c8660-2864-3d1f-96c0-fe9862e53c50 | -6.30113 | -42.36966 | 2025-09-21 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 08fac7d5-4238-3ee6-bac9-1025d53b1c57 | -7.72218 | -44.45038 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 028b3d65-5ede-3a2c-8d24-6c9bfa9552bf | -5.7619 | -44.19912 | 2025-09-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f547fa5a-7512-3f2b-a6da-53522e2d4c35 | -6.94349 | -44.74739 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e20ff74-d9ab-3018-b6d7-35f0f92fe1dc | -7.91517 | -44.1104 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 258e840c-52a5-391f-a8f6-91148cb83e1b | -10.28497 | -46.0717 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73f5b7ec-1f5e-3311-8b39-c0b812a7dd73 | -9.21628 | -40.23908 | 2025-09-21 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9da6ca1-5698-34f5-94d5-7f43af87552c | -10.28131 | -46.07105 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1da1540a-b3bf-3e05-b22d-2d13d027e5de | -7.73109 | -44.43976 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dacf381d-99ff-3dba-a05c-9b912a4e104e | -7.1915 | -44.45206 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16994fa6-d31b-3b6c-a512-0b0079bd090b | -7.72889 | -44.43138 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ed5903b-ccc5-324a-b1aa-a322191e0693 | -6.6767 | -38.49767 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52a1c131-687e-3ac5-a298-4c58a382cf11 | -7.8317 | -45.62708 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67f07e85-d734-3249-8349-e7a0fe197440 | -7.34995 | -44.54642 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70c677d2-6d8d-3d18-a8ee-f15dd8ada431 | -8.59952 | -45.34205 | 2025-09-21 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5a46cec-77a1-3e01-8e09-18eea67ad94e | -11.48599 | -43.56745 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4bd0075c-11f9-3059-8f0b-9b68327039e0 | -7.46427 | -42.63452 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86f7c98e-9751-3f1e-9da3-a121f463ce04 | -4.46186 | -44.13731 | 2025-09-21 04:08:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1cd9e437-760d-3991-9d16-e8becfd09395 | -7.92205 | -44.1115 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 399d3b98-c7fb-3161-8404-6cec37b4fe68 | -7.52168 | -41.33391 | 2025-09-21 04:08:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b5836a60-7731-3aa0-9120-c1313251e60e | -5.42397 | -43.25889 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6b615c8-96e4-3791-a958-7759f5672284 | -5.52888 | -43.8704 | 2025-09-21 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4c8def95-0dca-3939-b46b-28f9281d0c49 | -5.09495 | -41.16702 | 2025-09-21 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dfd6f9b2-8c11-3e63-8ed0-b97a273382ac | -7.61813 | -44.44244 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 706a2257-c50c-3def-b792-6065ea1ba9f1 | -7.71897 | -44.46991 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d0c9c5d-6010-3587-9391-8bb9fc836236 | -5.69756 | -51.76225 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c62e7a72-c221-3fac-b1c4-daa1ff530ce1 | -11.48323 | -43.56338 | 2025-09-21 04:08:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 410fa04e-a512-3432-99a9-29317a1e974b | -7.18863 | -42.24445 | 2025-09-21 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a17d5e2f-da32-3fb8-8758-2b8b8b4d8155 | -10.36376 | -47.88852 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bb929b0-f0b6-3727-b42e-84742c7393c3 | -8.35177 | -44.70649 | 2025-09-21 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55a674d4-7348-38c0-8f52-4b622c7aca74 | -7.79857 | -47.59743 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4024c43-422e-35fa-89df-cd364fa40848 | -10.29663 | -46.09187 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 63f05429-c2c3-306d-8007-a742b0dd702a | -7.92044 | -44.09964 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18401a6c-3a15-3eea-9e12-8604f631d8da | -7.80274 | -47.59814 | 2025-09-21 04:08:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2066275a-a194-3bd3-97c1-b51c8121fb21 | -7.61079 | -45.4851 | 2025-09-21 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44221f13-5824-3ec6-9b30-b8a57988dcf3 | -7.46096 | -42.63399 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9c4df18b-2b2a-306d-86b6-d70a4fdfd71b | -6.19232 | -44.05215 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3150b564-2474-3911-b592-295bea0b9bfb | -7.92266 | -44.10773 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce427db5-0629-3022-b65f-80c58437c451 | -6.67572 | -42.43354 | 2025-09-21 04:08:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d142a89c-8c2e-38cc-9946-463552895855 | -6.59956 | -43.59569 | 2025-09-21 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5edcd07-8699-3174-8ec7-a2116f935f94 | -11.26661 | -41.50107 | 2025-09-21 04:08:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57070f49-39d6-3651-a429-ad5a4a9d3210 | -7.29796 | -44.12632 | 2025-09-21 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb8896ed-94cb-3104-a0cb-908328ea97fe | -7.17926 | -42.23943 | 2025-09-21 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4663554e-8803-3979-aca7-5bcb425f0a25 | -6.84879 | -44.16687 | 2025-09-21 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70916250-207e-31ce-b967-249b033eae7c | -10.34743 | -45.22699 | 2025-09-21 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aca147b-77cb-32ce-9a7e-ae0a89f90732 | -11.27803 | -41.85001 | 2025-09-21 04:08:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dd89fe22-7f03-3257-b489-1ff56aa1a71c | -10.27058 | -46.1158 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28e6aa8e-a11a-33fa-84f5-10a50c816b4d | -8.83312 | -43.03807 | 2025-09-21 04:08:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d733bc75-5fc8-3abd-bc56-583ff6f378e7 | -7.93823 | -44.09864 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 36e0e642-b9bc-388d-a34a-7555fa402267 | -6.24791 | -43.75108 | 2025-09-21 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67355b5b-0d9b-3b24-90fa-d3621e92f121 | -9.92293 | -45.94595 | 2025-09-21 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ee79a85-4ee3-31f5-9208-beb090f1a125 | -9.17438 | -44.62509 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| accc0560-5abd-3815-94d5-23dfc512045c | -7.93641 | -44.10994 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 585553b8-cebb-379e-af26-028e8dc6b00f | -4.86002 | -45.89716 | 2025-09-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c48d9e65-272b-3bf8-a333-582ec033ed57 | -7.94328 | -44.11105 | 2025-09-21 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb34697c-7435-3795-a24d-9fa82f9316ca | -5.6983 | -51.75817 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18b03507-e619-35cc-a9b4-731b6f61d112 | -10.85302 | -44.35088 | 2025-09-21 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4467253c-9f96-3f82-8c6b-b104a7d83cc2 | -9.42699 | -44.7088 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cfbf31c0-544b-3729-bf9a-50deaf0dc87f | -9.16807 | -44.62016 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 408a6c4d-d7ca-37c5-9150-c1105caa824c | -4.56486 | -41.50588 | 2025-09-21 04:08:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e0edefa-38a3-3bc7-adf4-4def4d97270b | -5.69686 | -51.75704 | 2025-09-21 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 67dec779-d6f9-361b-be71-3d403c6bbcaa | -7.8324 | -45.62276 | 2025-09-21 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 464135da-ebb1-3d83-a44a-5d4c66b2d682 | -5.63338 | -45.94851 | 2025-09-21 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 56e3d627-14f6-39e7-9f65-b59599ac17e1 | -6.25477 | -43.7523 | 2025-09-21 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5a5c41-4900-3929-a883-4cb373d3784f | -9.42352 | -44.70823 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2ecb675f-5297-368c-bab2-1f589d9a6eac | -3.20361 | -51.59343 | 2025-09-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9c7a2bd-b06d-3144-bf68-f5a74b566ac2 | -10.35846 | -47.89484 | 2025-09-21 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3784ab3c-1c72-3eb2-a198-83fd1f27aeb1 | -4.6192 | -46.15844 | 2025-09-21 04:08:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df88f4e0-cc72-3728-847b-2a8f3ce00be0 | -7.60212 | -44.4961 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed326893-fbbb-3b5d-a960-a7936880fbb9 | -9.42635 | -44.71265 | 2025-09-21 04:08:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a43ffe92-dcdc-3bcc-a78d-1c1cf375c164 | -9.16397 | -44.62347 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 596c1a61-2989-31d2-9195-574256c0aef4 | -6.39184 | -44.63325 | 2025-09-21 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b82e5466-a7db-3eaa-8643-48bce66e5f16 | -9.12076 | -44.64802 | 2025-09-21 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c61b8e29-a588-33ea-974d-2bf9b1b28111 | -5.52001 | -43.86972 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2deb7108-a897-393f-a197-49fa986caccb | -10.26319 | -46.09193 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c401301-a963-32dc-9e15-781eb105609b | -6.06936 | -41.00284 | 2025-09-21 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bae25081-c8f2-3f91-bb2b-0dd69d5f63ac | -6.26057 | -44.08217 | 2025-09-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b6c55c0-6e30-34e6-987d-4743cf28783c | -5.14889 | -45.70826 | 2025-09-21 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a9491db-ecda-3a8a-a412-4d8681fd723e | -8.81169 | -43.02323 | 2025-09-21 04:08:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f36f5d38-05bd-3817-9781-50c07e3a03b4 | -5.52316 | -43.86167 | 2025-09-21 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2a73d172-c701-3ed6-86f3-9d00db489796 | -7.3531 | -44.57177 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c36b567-3591-3bac-8ec5-15d93ef2839e | -5.34415 | -43.36063 | 2025-09-21 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e72bcf63-ed74-317d-951e-4c56828d2d24 | -10.28788 | -46.07675 | 2025-09-21 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e74ab39f-f41d-3396-be00-754fe13bb2b0 | -3.76019 | -54.81184 | 2025-09-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 1e6fe36b-9218-3181-af66-b5a365e47dbb | -7.60563 | -44.49665 | 2025-09-21 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ef74d6c-c71c-35ac-ab13-713ab107abd6 | -8.71075 | -45.26079 | 2025-09-21 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a5fede5-d184-3649-a2e6-193309e4d0fd | -7.3898 | -47.04494 | 2025-09-21 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
