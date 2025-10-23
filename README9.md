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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff482fa8-6c5c-354d-b860-fb2097b3e2e3 | -9.97681 | -47.08668 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a91a397-9d83-3f0a-9afb-7c7a8e2b5b3c | -13.01144 | -48.45661 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e30a9794-8072-313b-a828-9b4a589c80f8 | -9.9307 | -47.46241 | 2025-10-23 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae49ecba-ccc8-3e44-ae32-7761462dece1 | -9.97441 | -47.07242 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12362af6-692f-3500-b110-4264add36b4c | -12.90952 | -47.74021 | 2025-10-23 04:08:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cafffdd-d9e5-37ab-9d95-f1e1bde6b047 | -12.6962 | -48.83927 | 2025-10-23 04:08:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65d590d2-514a-387f-86b6-e4dcf4ae4af2 | -11.0598 | -45.39412 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f53b4cf7-6a47-3011-a98a-ed56f0fed336 | -7.88565 | -43.55038 | 2025-10-23 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 675df7af-3815-3b08-94cd-7fe9e4d60411 | -12.70537 | -48.83677 | 2025-10-23 04:08:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c32f7f4f-1c88-3196-9c7e-e3e5e0cb6ef1 | -13.04507 | -47.21996 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a5ff9e2-c4b7-3c16-9918-94622a374cda | -12.00045 | -46.77812 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6afdc9f1-8ba2-3bb5-a5a2-dde3d672455f | -7.17254 | -44.78864 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc883750-3e33-3479-a441-fc001f7ead55 | -12.69673 | -48.64185 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae32a04f-c227-3e40-aab4-55125fe8aa81 | -9.97941 | -47.07117 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b46c693-db5c-333b-b82c-bf97dc6c24c1 | -12.0034 | -46.78346 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2846079b-eb14-3474-8cf0-a77e2db53bc4 | -10.25367 | -47.99589 | 2025-10-23 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73a97841-43fe-38c3-bf9f-ba528fdf8b31 | -9.08824 | -47.81701 | 2025-10-23 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7c25b86-3bd8-3d3e-85d6-551052df61ba | -7.89291 | -44.53236 | 2025-10-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ebf3fee-68ce-3e9e-ac43-35ef211527f2 | -8.00654 | -45.47229 | 2025-10-23 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc0ce95e-c339-3c8a-8497-b622c201e65b | -11.85362 | -44.03109 | 2025-10-23 04:08:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b5fb64b-7791-3a2b-97f4-9b971d88ffcf | -7.9447 | -45.25693 | 2025-10-23 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eab6f2a2-438f-3234-997e-04dc545614f9 | -13.29862 | -47.4816 | 2025-10-23 04:08:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84126010-b783-3e6a-a1d9-900b3fa66464 | -11.74178 | -51.18885 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1c56538-9b3d-3d04-a61f-35e220c5f12a | -10.25302 | -47.99972 | 2025-10-23 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 466a7009-eb6f-327c-99f8-52490b509279 | -9.08405 | -47.81621 | 2025-10-23 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba549d4e-2fa1-3148-8f94-bec54aca3fc3 | -8.44711 | -48.10566 | 2025-10-23 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57511db2-34d6-306b-9fb2-729bf5176ef2 | -6.32174 | -46.19783 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c7cdd72-dfff-36a8-8eca-bf7bba23c1b2 | -9.93006 | -47.46609 | 2025-10-23 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30c8fe3b-4049-3bb6-adad-0743093a5b01 | -8.87493 | -47.96875 | 2025-10-23 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f0183ad-cf7f-3cb7-af6d-0b14c385fde4 | -8.61499 | -41.41435 | 2025-10-23 04:08:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13f9cb08-0dcb-3829-8f6c-09e4c9bc3ade | -11.35284 | -49.79506 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ae33689a-8049-3d8b-8180-19359af17a80 | -6.92662 | -48.26485 | 2025-10-23 04:08:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22a7eeee-0e5e-3370-b1a9-58f622f7f7d5 | -9.35997 | -46.24077 | 2025-10-23 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd28f03-c73d-3a54-96eb-67fb7beb3f8b | -6.60041 | -44.22051 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f462fdfd-2d49-3274-8e39-1cbc51263d37 | -11.12963 | -48.34199 | 2025-10-23 04:08:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 131a2f99-d20f-37a5-9bf2-2e2cdeada734 | -5.28939 | -50.56837 | 2025-10-23 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3c75a571-fa8a-3c25-ad28-36a9d7db4e3c | -13.04889 | -47.22055 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f05f3041-6f2a-3d81-9048-8133ecc3d47d | -6.80979 | -44.00718 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b198be7-4053-3d28-bd04-cda50f9ca3e4 | -12.68005 | -48.63866 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 407944dd-6754-3cb5-8b49-ee34b379e577 | -12.68423 | -48.63944 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b2b274c-7d97-347c-9ae8-898706b6eb18 | -7.67017 | -46.58549 | 2025-10-23 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd98581f-8d27-3692-8ba8-b3e4922c702b | -13.04256 | -47.23436 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6a3b778-bca7-3b7b-a96b-2d0da78ec712 | -9.45832 | -40.39141 | 2025-10-23 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e6399d5-1f55-3cfb-9d70-70389d9c0fe2 | -11.12541 | -48.34133 | 2025-10-23 04:08:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5c56ae5-80dc-3f34-aa38-7f4b3a015e6d | -11.356 | -49.79824 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0a872c32-5154-3f8c-9396-e38d2f14e8ac | -7.3597 | -45.04549 | 2025-10-23 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfca0d2a-3dd1-3683-a01c-4730cf17ace8 | -6.96365 | -44.01604 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 79526152-a6b9-342d-b4ca-8649211a403b | -13.37134 | -46.63932 | 2025-10-23 04:08:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fdaa216-edb8-3b43-88c2-3572327e78ab | -11.99497 | -46.78426 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad777dda-92c5-3bb0-95ce-078f4440bc51 | -7.62898 | -42.19461 | 2025-10-23 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d096dadf-292e-3fa2-9763-ac6be8ff8c5f | -11.99669 | -46.77746 | 2025-10-23 04:08:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c99902c4-bb26-3142-8ca1-20fb3c62973e | -9.35997 | -46.24076 | 2025-10-23 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 820a7778-614c-3177-8104-b4fb8490d0d2 | -10.91169 | -50.11164 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20c1ba1b-6ff4-321c-a75f-44ba16eab248 | -10.25302 | -47.99973 | 2025-10-23 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85535826-4b27-3ddf-ad7c-ca3737aea36c | -9.62788 | -40.33436 | 2025-10-23 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 38938104-227a-3388-9b85-d6a45a0a588b | -11.36241 | -49.78938 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c39587e0-e302-3d15-8774-18c62789be1b | -9.35936 | -46.2433 | 2025-10-23 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 976c76a8-c713-31f4-b5e6-0dee4859d8f6 | -6.94567 | -44.46278 | 2025-10-23 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc1b8dcf-b509-361f-8741-6b6536ddc9d3 | -6.60041 | -44.2205 | 2025-10-23 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2d8c6ef5-0e69-3c25-98dd-00f94ae2a3c2 | -6.84877 | -48.2608 | 2025-10-23 04:08:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c66f337-3cb8-3466-9702-2c356389afba | -12.8239 | -48.66095 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08e6e506-1722-34be-88db-ec7204bafd26 | -12.70043 | -48.84002 | 2025-10-23 04:08:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92cbe116-3062-30cd-8744-26629e5f312a | -7.27954 | -44.21681 | 2025-10-23 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a07070ae-81ef-33e6-870e-6917ba7aded3 | -13.01041 | -48.45599 | 2025-10-23 04:08:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7959204-6cf0-3867-a421-0900975c02c4 | -11.0075 | -47.67643 | 2025-10-23 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cf551ea-bcf0-320f-a7af-58098ad31815 | -11.80647 | -45.18314 | 2025-10-23 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2202315e-4e52-327c-92ae-c8f6750fe7c6 | -13.03959 | -47.22894 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3e1fc47-0a70-35f5-b0fc-cb5277572a57 | -10.91074 | -50.11683 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db99a4d0-4794-3dcd-9d09-d59899a162d5 | -12.69184 | -48.64505 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bcaa17d-d3ac-3042-833e-da80a6659d81 | -6.32447 | -46.20066 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 215498d4-8201-3764-ab03-1c10710664a3 | -6.96427 | -44.01218 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5bba10a-c614-3161-8453-8f87006113a7 | -12.67319 | -48.62893 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3025a7be-ed08-35ce-af1d-951c57f878c1 | -11.01357 | -47.57088 | 2025-10-23 04:08:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f4731a6-9dc6-3cec-b0a1-ebc6cd756a16 | -7.15859 | -44.202 | 2025-10-23 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 605de4cd-aef3-3e11-9e42-123164c8b5d2 | -7.27585 | -49.99183 | 2025-10-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ede7e78-2a3b-3a51-ad31-1e8736a077c9 | -12.24964 | -49.58911 | 2025-10-23 04:08:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dbc5d1f-2af4-33f4-81d7-b252006636cf | -6.96801 | -43.989 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f9558d0-e98f-3333-ba0e-6fb184c45fd6 | -12.89914 | -46.9832 | 2025-10-23 04:08:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f9ce341-7bb8-3c7a-ad76-33f48101f78f | -12.69256 | -48.64104 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c268e34b-ee9e-325e-8f13-2a959a25e05a | -9.9735 | -47.07759 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 508d5272-2a97-3a34-89fa-13e70e19f669 | -8.22123 | -45.49146 | 2025-10-23 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6be9f774-bb9c-3fdc-b303-2c9987bbd8c0 | -12.25195 | -49.58876 | 2025-10-23 04:08:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 655e0f5e-a495-3ebf-9536-9c553a85e5ec | -9.97546 | -47.07051 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dcdc490-27d2-33b6-9ca4-835bed6aa8b4 | -6.96775 | -44.01273 | 2025-10-23 04:08:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64e2fe4d-ad7e-3b22-b595-96ba1aca2df5 | -7.3246 | -45.28448 | 2025-10-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ded35ed-63ae-334b-83c7-03aaeb9ed51e | -11.0598 | -45.39413 | 2025-10-23 04:08:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6303f06f-f022-3db6-b917-945f1246d2f7 | -12.7837 | -48.57381 | 2025-10-23 04:08:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fe0937a-5c75-3dc6-b0f8-ee72487612dc | -7.16209 | -44.20262 | 2025-10-23 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feb4d630-fbe4-342a-a591-b9e5c354a076 | -7.30486 | -38.25272 | 2025-10-23 04:08:00 | NOAA-21 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9540ddf4-671f-3152-ad9e-8be0e0a6a988 | -9.23234 | -45.60135 | 2025-10-23 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bda8bfe-85c3-32c8-a5ef-2992a2f195f4 | -7.27954 | -44.21682 | 2025-10-23 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd792dfd-2f4b-3719-a3f9-2e661bf137bb | -11.35229 | -49.79256 | 2025-10-23 04:08:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| bcb5cc25-2805-3374-b587-a4f726fb802a | -7.88624 | -43.54671 | 2025-10-23 04:08:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1df8f641-e30d-38df-a34b-59fac843b25b | -9.97259 | -47.08276 | 2025-10-23 04:08:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 127817bb-793c-3de8-931c-51ec9b752b4f | -11.00359 | -47.79438 | 2025-10-23 04:08:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f618461-83f7-3119-8958-d6afb2f2bb51 | -11.14241 | -44.94128 | 2025-10-23 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fd510b4d-31f9-30ed-92e1-629714e7f254 | -12.25413 | -49.58993 | 2025-10-23 04:08:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3059c457-bcfe-3605-9143-b1b16fe1b848 | -7.88905 | -43.55091 | 2025-10-23 04:08:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 787d1c93-bbe0-3b0b-94d0-17b3ddc41fcb | -6.90844 | -46.13249 | 2025-10-23 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| def38e3a-9e9d-3f7c-aabe-974ded01c42b | -13.71986 | -44.66134 | 2025-10-23 04:08:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README10.md)
