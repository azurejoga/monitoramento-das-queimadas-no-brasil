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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d58919eb-1565-30b0-9421-6cd1b8ddac83 | -3.23616 | -43.22409 | 2026-08-15 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ee9b483-0af0-3970-b2b4-df938f85da6b | -4.52625 | -38.55049 | 2026-08-15 03:51:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7ca4ce4d-d77e-3551-8e95-85141a6b32ab | -4.36386 | -37.89774 | 2026-08-15 03:51:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27d6c28d-52d3-3de6-ad24-3b69197c4b45 | -4.10197 | -42.50263 | 2026-08-15 03:51:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7c5b58fd-ffd7-386c-9a1f-4f03422196df | -5.19498 | -35.84907 | 2026-08-15 03:51:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7cfece8d-7d90-3a0f-abd2-5a51aef07f07 | -4.10948 | -42.50558 | 2026-08-15 03:51:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 7820ac75-a040-3465-ad56-ca6939c5a68d | -1.57974 | -47.75665 | 2026-08-15 03:51:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9d9bb8c-0e8b-3c58-8810-5efcc8099a37 | -3.23565 | -43.22719 | 2026-08-15 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3843371c-83d0-338d-adf4-ec6c37b8394f | -4.39343 | -42.33781 | 2026-08-15 03:51:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 712f666e-e21d-3d63-8f66-51268e4baaff | -4.10594 | -42.50879 | 2026-08-15 03:51:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ed8fc29a-db26-38da-803e-96ebec82e4a8 | -4.10683 | -42.50344 | 2026-08-15 03:51:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2bdd92e2-8e4d-3f9d-a84b-0b625c7bf0e2 | -5.51269 | -35.59602 | 2026-08-15 03:51:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f4b9bb4-8af1-33be-959a-be1671791caf | -4.09227 | -42.50098 | 2026-08-15 03:51:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d88607e5-57a4-39f1-b139-74b5afea7384 | -3.41805 | -43.1661 | 2026-08-15 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38be4d34-25b6-3139-8d19-1b44ba30d71d | -3.42318 | -43.16696 | 2026-08-15 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5813ea3-1f01-3296-9d45-8ad6be616b00 | -4.95427 | -37.93713 | 2026-08-15 03:51:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d1e7051-296a-300f-87d1-df47cd81723f | -1.57267 | -47.75555 | 2026-08-15 03:51:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50cb25a4-04f7-3c14-8cf6-6844eab86074 | -7.27747 | -44.67895 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79e58017-ab56-3123-9878-099be9f8abfd | -6.84026 | -45.37722 | 2026-08-15 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c09e44e7-5196-3d23-8bcc-aa9f903b6857 | -8.52226 | -46.52733 | 2026-08-15 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c46f773-4eaa-3f54-979b-082351038ff0 | -9.12414 | -46.401 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aebb13ba-fdef-301a-af3d-c3b0bc0eabac | -9.11845 | -46.40196 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e0db7568-5440-3c91-b62f-81299dee0166 | -7.36549 | -46.81715 | 2026-08-15 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d76398e1-e8da-320a-af38-60bc4d67f1bf | -5.3411 | -43.17736 | 2026-08-15 03:53:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a83e8abd-bea6-3bf9-8868-db6480abf925 | -6.9819 | -41.29631 | 2026-08-15 03:53:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e8641a23-575e-30d5-876b-7f0ae233c13b | -6.86031 | -41.64045 | 2026-08-15 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4d40a084-e1df-3b2c-85ea-b114052bc964 | -6.11643 | -44.03411 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| aa5a9ad5-95a8-3b1b-bf30-1150b0560a78 | -6.93281 | -43.63272 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 36aa3d5b-6665-3e13-8a3d-72061d165374 | -8.71603 | -49.60029 | 2026-08-15 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f220cd1f-cbc5-3278-842c-58f7d1c28f91 | -7.61927 | -44.15103 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 454c91be-f6c8-3f3c-a461-52fb537f0de7 | -8.62428 | -45.85482 | 2026-08-15 03:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b666f06-5bff-3606-95ac-93789cb6c35e | -7.00592 | -41.44124 | 2026-08-15 03:53:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 588bfb31-f27c-3b4a-9cb3-f78507893910 | -9.1176 | -46.40389 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6ca909e8-35de-355c-ad9f-85b652421dd2 | -5.66813 | -43.57456 | 2026-08-15 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97ca50bc-7527-300a-a7ce-26b31e309fe1 | -8.52306 | -46.52303 | 2026-08-15 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5534d033-7a13-3701-8913-6a5d1cfb054c | -6.11754 | -44.02828 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 143b4ab0-29cc-388d-b15d-ef66196860db | -6.85985 | -41.64175 | 2026-08-15 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 87148d4e-4702-3774-9a9c-479f1511e0f0 | -6.86537 | -43.87171 | 2026-08-15 03:53:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc70e2a0-f527-337f-8920-84d8206b443b | -5.67113 | -43.57434 | 2026-08-15 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dca8fb93-9ae3-33e2-8c69-d96fb6bdd10e | -6.1227 | -44.02947 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 44e52687-4803-3815-a7a8-c62ceb6add93 | -8.72172 | -49.60855 | 2026-08-15 03:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be1a373d-57f4-39c8-ae06-3c8710f26f99 | -6.34058 | -44.07467 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f798f00-f786-3171-80b9-be30b3fba9c1 | -6.12169 | -44.03535 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c25cd51d-306d-3d1e-9d6e-9c9625868973 | -7.36465 | -46.8216 | 2026-08-15 03:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1256c825-0b3b-3360-a77b-b81f370d278a | -8.06904 | -35.61216 | 2026-08-15 03:53:00 | NPP-375D | PASSIRA | PERNAMBUCO | Brasil | 2610509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 0b5c6d9f-ec19-3ae3-a0c1-2e97a4e51a34 | -9.10693 | -46.39956 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ecf9524-718e-3c1b-96b2-deebdb426ab1 | -6.11703 | -44.03122 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| da81f200-9b33-3a4e-ac2d-acacbb4b1bae | -9.10616 | -46.40371 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9b45fb1-16bc-3d5f-bcdc-6aa26d3cde53 | -5.93193 | -43.64325 | 2026-08-15 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 917759a4-c8bb-3d18-978d-890d1690ba64 | -6.93069 | -43.64443 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 413b0cb3-c476-3546-a08f-832b913e07f9 | -6.93995 | -44.54576 | 2026-08-15 03:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf3fe57b-9d0e-32f8-96a2-437ee60db935 | -9.13645 | -46.40161 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8401dc9-0965-3912-9ae0-3928187dc248 | -8.16646 | -47.40315 | 2026-08-15 03:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3e6971bf-03f5-3853-981f-cc773b6ef2f7 | -6.12212 | -44.03228 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 734ebf4e-9413-315a-9098-1cce85856ab5 | -9.11836 | -46.39996 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| af8d28cd-75b3-306e-9d88-b8cf08a7c6d2 | -9.11382 | -49.27102 | 2026-08-15 03:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db42a463-4c42-3e23-ab75-9719af058630 | -6.83878 | -41.66007 | 2026-08-15 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0d1e80e4-6ba0-3e8a-b1f4-32ad5d0d7ce9 | -8.56157 | -45.34283 | 2026-08-15 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f2f036f-e0e6-3733-8b9d-00f7d08ff7e6 | -9.12421 | -46.40311 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0254eeb7-0573-3b10-83ef-7439a5c152c7 | -6.92717 | -43.63659 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 1813a8dd-4ca4-3b5c-a5ce-fe5c2a2309e2 | -10.75945 | -42.09061 | 2026-08-15 03:53:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7a79803-77c7-309d-8e29-83c590d81a8e | -5.4902 | -45.1247 | 2026-08-15 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c747a573-24bc-38f7-9e8b-e6237fc6318a | -5.66552 | -43.57645 | 2026-08-15 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90bec63a-ddf9-362b-a7b2-c36188a718d0 | -8.16938 | -47.4016 | 2026-08-15 03:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 66eed443-f9dd-3099-8d68-79e2de2f5145 | -6.33646 | -44.06768 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 101c75b3-8029-361a-831f-31f660f4d229 | -8.49202 | -44.73935 | 2026-08-15 03:53:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcc905df-5f3f-3dfd-a2c2-7fca06b6bcec | -6.34003 | -44.07774 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 139082a8-30b3-3724-b9f2-af83b7629bba | -8.17272 | -47.40425 | 2026-08-15 03:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 77f34f38-5298-3481-9ff2-4126157efda0 | -9.11765 | -46.40623 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0b40c976-6032-3b46-8e25-9e7e35129c81 | -6.84287 | -45.36311 | 2026-08-15 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 958eb0e5-7f4c-335b-9d30-25a949eb1271 | -6.92569 | -43.64357 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bab27ce1-924c-333c-82e0-5e17249574d0 | -5.49094 | -45.12059 | 2026-08-15 03:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ca5015f-d4d4-3108-97c2-07f6672eecf1 | -8.16846 | -47.40648 | 2026-08-15 03:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7f307da9-6501-321e-8895-6ff991c28b48 | -6.11696 | -44.03112 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2083eb1e-237d-3a65-84d9-00a59ecffbe9 | -7.72828 | -46.24895 | 2026-08-15 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6048060d-2c2a-35ad-9277-6dbdff73a243 | -9.11258 | -46.39889 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3319d092-5ffa-30c9-90bb-a1073ae739e3 | -6.93176 | -43.63852 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 727b2108-53e7-372a-b16a-3e454755568e | -9.13644 | -46.39925 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb370a1c-bb2f-3ebc-bf3d-c3eb96988e1d | -6.33586 | -44.07081 | 2026-08-15 03:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e44e952-2878-39db-9561-5080ecbb0002 | -9.13726 | -46.39498 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adf6237e-fc30-349d-9250-12c6cc8a8abf | -9.11503 | -49.26478 | 2026-08-15 03:53:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91c43a36-aae2-3959-bddf-e5eece6d9f87 | -6.88265 | -41.95828 | 2026-08-15 03:53:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 43561afb-2fb9-35c0-ad8b-ce1c98224001 | -6.99633 | -44.83288 | 2026-08-15 03:53:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3ea35e0-81aa-326c-86d5-5bb29368d442 | -6.83442 | -41.6592 | 2026-08-15 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00596955-1fae-32f9-a3de-88c800047bf5 | -7.82039 | -44.11507 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dce08ec-ce69-3f2e-8bf3-e34990a3b91a | -7.01328 | -41.43353 | 2026-08-15 03:53:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 36b2a540-15a6-3014-973f-a16790ca17f6 | -9.12337 | -46.40768 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae371dd6-2d02-3097-95b7-32a647a97807 | -9.11266 | -46.40092 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0dc35dcd-1edc-346d-b00b-4fad13513454 | -9.58179 | -45.36786 | 2026-08-15 03:53:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe143e9b-993e-321d-a054-43afc1b5a49b | -9.11181 | -46.40285 | 2026-08-15 03:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d101a222-1a5d-3828-a0ff-5bb67e099ed5 | -7.27861 | -44.70365 | 2026-08-15 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1095454c-93d7-3a75-b282-c9180535ca8e | -7.81799 | -44.11449 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2095ed96-05c1-3950-b83e-fbf0909bc0ee | -5.1157 | -41.10082 | 2026-08-15 03:53:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6097db11-7d6a-3a23-8053-856119d33630 | -6.92677 | -43.63762 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 56c1649b-6ef4-343a-afef-c7ad73583dea | -9.57578 | -45.37033 | 2026-08-15 03:53:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47f02de9-cdfe-3802-8367-3986b4044d00 | -7.8231 | -44.11523 | 2026-08-15 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75dba3df-e23d-3a92-a646-18b5c0dfb0cc | -6.92782 | -43.63181 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| c2814d2f-03b9-3b55-80c0-35b699028508 | -6.33701 | -44.06464 | 2026-08-15 03:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43050230-1190-3081-99e8-c961f7b6b01c | -9.5684 | -45.38005 | 2026-08-15 03:53:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c049cc76-21fc-3758-bada-6f35037461ee | -6.93114 | -43.64342 | 2026-08-15 03:53:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README8.md)
