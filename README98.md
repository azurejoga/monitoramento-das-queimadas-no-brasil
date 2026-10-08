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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2d3dfcf-f268-35fb-8669-b3125fd39279 | -4.54762 | -54.97224 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 105a502e-4cae-349c-bc83-e1126176fc7d | -4.06811 | -51.03684 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5976395-ebfd-3261-a5e2-8b7e48192ced | -3.594 | -54.57645 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18110fa3-dced-32da-9d2b-cbcdacd67a5b | -5.73133 | -45.1473 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3958c527-458f-37f7-b8a9-5f5c7a4ca388 | -5.7332 | -45.16407 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a5e20f8a-0d6d-3bcb-b535-ce95754066e4 | -7.38542 | -55.2074 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e4c991c-31a9-36fa-8a82-c026848e69fb | -2.72551 | -57.46563 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88826aa4-f798-3939-ac9b-1906bafe0bd7 | -11.6315 | -43.70555 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdc3e87f-c4c6-31a0-a724-388d7a696972 | -6.95844 | -45.26613 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd327bf7-3708-35e2-a5b6-37099f619679 | -3.28865 | -54.02103 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0dc4281-006a-3222-8bfd-f5b4447e8434 | -4.53763 | -54.98536 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6cea89d3-3900-32d4-a057-925a472cc322 | -7.89954 | -44.17493 | 2026-10-08 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eebdd31-542d-315a-98ee-f0f75df47b79 | -11.63065 | -43.69244 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2232dc2c-f7ab-3530-8159-8b777638fc30 | -4.77607 | -55.73319 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa22da65-b8aa-32ea-9df4-801e58da1108 | -4.75309 | -55.65728 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 064304ad-b4ad-36e8-ace6-f469accba731 | -3.26504 | -54.0041 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 380bd302-f7f4-302e-bff2-a229d03cc83a | -11.46122 | -43.38636 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c2b61fc-c804-309c-80e7-db7365711fc2 | -2.93407 | -54.1694 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05e906a3-ee60-34cc-af35-32d17f4c4608 | -5.85724 | -53.46195 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a8bb57c0-ea0a-3628-9b1b-841d0f5720a6 | -3.67422 | -54.27943 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03e75b0a-601c-3f7b-9913-97bccd950b84 | -8.74032 | -45.16181 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc535920-e211-3744-9194-2f23d6b0b457 | -3.22729 | -53.88883 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ec48753-a786-3d27-b1aa-62d130dded6f | -3.03086 | -53.9435 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c0d363d1-517b-3e66-994c-e2d417d32ac3 | -3.29022 | -50.43979 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bfd7b4b-f6fd-3f9e-ab1f-a0932ad8df95 | -5.2118 | -56.07889 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a8a9a7e-975d-3f99-a05e-158d4551e1c4 | -3.35987 | -50.47517 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dd585f8-44c3-3d1e-beee-e421d83d6402 | -7.03889 | -46.59752 | 2026-10-08 04:46:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5964e99a-b2e1-389e-9787-a91d61760dd4 | -3.56328 | -59.47754 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 832ac112-a9a2-3b68-8f8d-e5867e33e188 | -3.57628 | -54.66319 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24b8de6f-2c0f-3b9e-a348-28ac5bf8f350 | -4.52334 | -54.98036 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 400ba9c8-0cdb-3154-a6c3-4ca65c9e2788 | -4.94178 | -49.2187 | 2026-10-08 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3d61103-4716-3a54-815c-c7b1dd30cd72 | -3.01203 | -54.74321 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94ba33d0-a3aa-3944-a7df-e01da6796a98 | -5.48808 | -42.86016 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0fac11ab-19e7-3133-8401-3d81074ebc0f | -11.15264 | -47.29261 | 2026-10-08 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da74a2e3-2603-3bc9-9ef7-7588d9fce03f | -3.53764 | -54.63813 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b45fac76-6fce-3eff-80ae-7b7fca0e3697 | -4.24435 | -51.04326 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a3c7acf-227c-3201-b6db-61a1d529ea9f | -3.22 | -53.88775 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75609f78-8530-3476-9901-c9ea70d2d7f1 | -3.44994 | -56.93872 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98b92432-29a4-3c86-b98e-183a759b81b8 | -2.4796 | -56.0895 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a57546b-46ae-3e8c-b4ac-f0fcb1baae3f | -3.2734 | -54.68817 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bd38787-f418-3e45-8423-5e53ed485269 | -3.56693 | -59.48799 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 966c3ac2-a944-3852-907e-d8fe2692a9e0 | -3.08771 | -54.26901 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38413b33-3da6-3da9-87fd-f3a54256f5ef | -4.93767 | -55.80981 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c0fc656-f88e-3a48-ab7b-b1f65035355b | -3.47727 | -54.62619 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55f563b6-7276-3675-a94a-66d6dd8485a4 | -5.70482 | -53.4897 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2e98664a-d829-38cb-9075-bdcda97cc6f5 | -3.11116 | -53.77209 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02e02074-5d7c-3d98-8b72-0a78864985f9 | -2.94555 | -54.10535 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e36ec9b-cefc-3467-9107-322decd0bb92 | -6.99845 | -59.12004 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eea9132b-5acf-3327-9f26-45fd05122498 | -7.22784 | -55.1659 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83b296ea-5ce8-3ba1-9b69-0d8d85a475c1 | -8.22131 | -46.3514 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 073e10e5-552d-32ce-938f-2cc95bdbc959 | -3.281 | -53.83231 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2039a6c2-e0f0-3428-a4d4-673059316e5e | -2.93453 | -54.17589 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f47e3cff-07ee-379c-baee-be613828bf5e | -8.21626 | -46.32826 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 92d4a74f-b796-32cb-a75b-1d63ea9df8a1 | -3.53605 | -59.47971 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4fe12b5-3251-3c3f-8fe3-6bd067d94236 | -4.11557 | -59.88413 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 87c52ae1-f1f6-39a9-a536-b18aac37c46f | -11.39553 | -47.55531 | 2026-10-08 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09e3e7dc-abfc-35c1-8b55-4848847bd7a0 | -3.30583 | -54.05316 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 24451a2a-f114-34da-80b5-b42c7f8b93c7 | -5.70542 | -53.48598 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 029a08d2-5758-3d91-a5f2-673222b56e53 | -3.28768 | -54.00323 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14ac7a91-9f2b-33e0-913d-768f3057c084 | -3.05623 | -54.22756 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc338e79-dbf9-38f0-902a-087809edff8e | -3.04659 | -53.91524 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72eca93e-e06d-3463-9e7d-492b92141d45 | -10.88356 | -49.15043 | 2026-10-08 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ae3eef3b-704f-35c2-9c9a-95f76e1abad6 | -9.8034 | -48.91714 | 2026-10-08 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae63619d-68ca-34c9-be3a-f4596fbd59a7 | -6.10398 | -55.71759 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52a6fda3-565e-374d-9ee6-0f350089117d | -3.58385 | -54.66441 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b32353e6-cc03-3646-9acb-2ae2213e6f91 | -4.1209 | -59.88498 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b7683881-8c62-3741-b9df-31cd7b630fbb | -6.94612 | -45.29089 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7522a782-5cd2-3778-8032-89b943d7a171 | -2.89125 | -59.207 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c2ddee9-711e-3ee9-86b8-b8b5baab9276 | -3.00861 | -54.05962 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| afc8d1f1-baac-3776-afcf-0f7495ceb783 | -2.76627 | -54.09629 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb7099f1-9a73-33f2-9fef-2bf4c19a6cf5 | -6.02377 | -53.8515 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ce7b68e-23ac-31db-b343-2131ef7a0fee | -2.49459 | -56.10403 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c892c608-76d8-316a-a34c-04ef0945ba7e | -10.96213 | -45.39303 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3af00cf-c660-3cb5-8b89-bdb741a1f317 | -5.6852 | -53.47881 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b252fea5-57d4-3f16-a487-52b3daa00ace | -8.38476 | -46.288 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa33f259-bec7-38f1-bba9-6106e71f5e18 | -3.28327 | -54.07628 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 496c7929-22df-3d51-8200-46001911328b | -8.7112 | -45.20742 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5ad64fa-25f8-3537-ab9e-9bbe959a8949 | -4.26947 | -54.86765 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34b94ce7-ddaf-3fb8-89c6-3d35e2b964bc | -3.30197 | -54.03053 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2803a6b9-811b-3924-a378-30ab09b6610d | -3.21563 | -53.9613 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7496a152-1dbc-33e3-bb69-7c1a16b15eaf | -5.65849 | -49.73634 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b415f92e-7f1f-329c-953a-c19258648b0b | -3.44185 | -50.62548 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65393d2e-cebe-3286-ba8f-9f920aae9963 | -8.29279 | -50.2709 | 2026-10-08 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80bf2506-6efd-3672-8ac5-66c97ec3a76b | -7.21667 | -55.16433 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b5f7a57-fd2d-3dd0-a984-0a2d86ed68dd | -11.63426 | -43.70501 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bec1db22-5d74-3edd-a509-8a1cf2033f59 | -3.85375 | -55.97656 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dba4a228-592f-3661-b76d-e249592d62d5 | -3.49008 | -54.6188 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbad0437-6288-3435-bf62-daadf03780c1 | -2.49439 | -56.16011 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b47260f5-e5b7-3ef3-9795-ee2c64b950b5 | -3.47194 | -50.08529 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d79ce6f-9a70-35a8-9d1d-1f77aac2e108 | -8.38366 | -46.28696 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d93c62c4-868a-3318-9d35-94ae15f77082 | -11.63386 | -43.70814 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd82941f-263a-3c14-bd8f-17a4c92a69d8 | -3.2573 | -54.02937 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ef28fef-4001-30d4-b9cf-c433f441299f | -2.99234 | -54.13786 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a80785f-5e3e-35d3-9b5c-6c183cad371d | -3.08454 | -54.24109 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7708f15c-4c1f-3062-bd21-bd9267d6f8dd | -3.02081 | -54.10181 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 750a5751-ac53-3d98-9ea1-a5e610c30231 | -3.5244 | -59.35751 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d00500a-1de3-34b1-98fe-38829873439b | -3.05919 | -53.93029 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 725494c2-6dd1-3dcf-8e8c-71ef2983ffc8 | -3.34998 | -51.62372 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74a5f942-7652-3690-b51d-2cd051daced7 | -2.94364 | -54.15734 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 781b47f8-15e4-3bf4-ad1e-cd5d9c61c57a | -6.80686 | -55.29771 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README99.md)
