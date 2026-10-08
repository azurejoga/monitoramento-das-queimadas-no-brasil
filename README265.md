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

## Dados Diários - Página 265

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c5a2e0e-a3d8-328b-9d87-d0a8c6b00350 | -13.1257 | -46.36728 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 4aab6b62-744b-3270-b5b8-84f30cc2c4c7 | -11.91899 | -46.80531 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3efa7223-7fae-3ebb-b26c-76f87feee37a | -9.55557 | -45.63754 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 05e294c8-da37-3937-ab12-293c0529f030 | -12.51641 | -38.73027 | 2026-10-08 16:18:00 | NPP-375 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 04ef2fee-999b-3f8a-87ca-2005d5977986 | -8.94486 | -45.15796 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 964ee451-ce30-313d-8f92-02828539eafb | -9.23583 | -46.46368 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| de184560-cedb-3098-a1b8-4af0a9e766f3 | -10.48814 | -47.2263 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4d0a05e7-a4f2-37a1-9d8b-7a6aaa55d945 | -13.98206 | -44.83208 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 11f29658-f095-3a12-b396-5eea76462ef1 | -8.59175 | -44.87269 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 858c4646-d309-3100-8a28-1f010c5bb2e4 | -8.28743 | -45.71949 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3cf78711-b260-39d3-9d58-53b15ff04b70 | -12.0368 | -43.43496 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 58942267-3f1c-3770-a64a-c3b2b6b84cfd | -11.40182 | -44.96234 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1fa90224-8252-3bd2-9886-09a2cc4fb5b3 | -10.76787 | -46.60324 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70083354-7343-32e7-855d-16abd267fa57 | -13.65209 | -47.67414 | 2026-10-08 16:18:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8217357-0a13-31e8-a5df-35727787b65f | -11.24879 | -45.25229 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f2a73bc-4bfa-356a-9e3b-d276a90639e4 | -8.96002 | -45.14368 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 704e37b9-b91c-35c7-8767-d28e72468513 | -11.91698 | -46.78944 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6e008e39-fdb5-3f6c-a715-e1c2a9cb67d9 | -11.20805 | -44.8696 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 446b3e3a-e5bd-3c10-8e7a-944367f8d6bc | -11.26315 | -45.18268 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b4a22122-5c74-33d3-ac21-606e177fff42 | -11.84988 | -47.36026 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 496c552b-068c-39ee-b8fb-37cd8195e326 | -8.12643 | -35.91712 | 2026-10-08 16:18:00 | NPP-375 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 01abb097-ee69-30ea-9029-8ff31b89bce0 | -11.30113 | -44.83103 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| aade489b-d4c1-303c-97f7-67186c6a5971 | -9.22917 | -45.65819 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 511c5f2c-4e12-32f4-bc4e-84cf6b75fe3d | -9.43748 | -41.73805 | 2026-10-08 16:18:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 1268c678-d721-39b7-a804-a057f9c0c3fb | -13.13916 | -46.34995 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ea83f858-1617-3ab6-86ad-039c3d77714e | -10.46872 | -47.2408 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| c571f8e3-a1f6-3778-bfe4-df882c44388b | -8.52701 | -46.91446 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 221ec149-3389-312c-b6ff-335e83edfa28 | -10.45784 | -47.23902 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6d67bf49-359a-360b-bc6d-10026b88c50f | -12.24337 | -44.74652 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 43453a97-3fa7-312d-9392-59bbdc80c141 | -11.60125 | -43.6687 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f9808f52-62af-3950-b7d9-ddd56b8ef12c | -9.82953 | -45.76979 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2617c0ba-1330-3b6f-8897-3e7f6cdeef05 | -11.13669 | -46.1577 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c920e0f2-c31c-3e5b-ae24-5eebd7a56381 | -8.94028 | -45.18988 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 8b170100-bfc7-34c3-b99d-f5c32fb5dd77 | -9.38986 | -47.09653 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c1cedb6-6404-316d-8934-68639c33d9e6 | -11.39877 | -47.56372 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd38cbbc-55c2-3324-a39f-76addc863a3a | -11.64663 | -43.68939 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 54f8d654-7f35-36ea-b8c6-9bebffc5b7b9 | -9.883 | -44.86512 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 536082cb-453d-3265-97a5-6a2f850e304f | -8.992 | -42.33862 | 2026-10-08 16:18:00 | NPP-375 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| abeb5161-b078-33cc-a60c-785996a94c70 | -10.44333 | -46.8436 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6143534c-f57a-3992-9f13-7803f0114e2a | -13.98267 | -44.83693 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f76812a5-c2ad-33cc-9875-1122f5546f54 | -13.26618 | -43.99919 | 2026-10-08 16:18:00 | NPP-375 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4e97f505-1d01-3e69-a434-ba294d31a835 | -11.59393 | -43.6774 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 37b2ead7-90f2-321f-8847-c50ab4103cb2 | -8.59159 | -45.69598 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fc0a1383-a3dc-3f40-8595-9a5646f5d878 | -11.39504 | -47.56278 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5f8469a0-1873-3b09-8ef9-e33f0ef5860d | -13.61418 | -48.19776 | 2026-10-08 16:18:00 | NPP-375 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60f6f7cf-95f9-3922-a14e-bbaa54a597e0 | -8.62077 | -48.35331 | 2026-10-08 16:18:00 | NPP-375 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6e7d8912-b7e6-34ea-ac06-887e85bd6a50 | -8.29496 | -45.73818 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1ab56f13-1681-38cb-861f-ada941a84883 | -9.83246 | -47.46663 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 93e5ccd9-136e-3cbc-892e-fdb7e4be04ff | -8.78761 | -47.26132 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7a5c83ca-9167-33ac-87c4-1c6761f65d71 | -11.78937 | -43.53532 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b9f5b982-d1de-36e9-916e-50a4d254f2ba | -9.35535 | -46.57472 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| c141b550-da1a-35a9-a8d1-6aa069bcf3a7 | -9.23886 | -46.46575 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5feac086-885d-380e-9074-d3fdbc8da3a1 | -9.94037 | -43.57633 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c2211680-b10b-337b-b209-dfcd438d8e24 | -10.44793 | -47.28683 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 43c69050-0c21-345b-a53f-a0472bc2ecb7 | -8.84262 | -45.45401 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 7c48e1b5-3993-3825-a4b2-d3571f8c9dea | -9.90225 | -44.81495 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 917ff81e-3873-34c0-99da-b06d5907df28 | -12.83638 | -44.62516 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 48975a8e-04bf-3c62-84c6-73fa9080230e | -11.76288 | -44.94906 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f63a30ab-f7e3-3e2a-81db-a6ae9e347a93 | -9.89095 | -44.86472 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 60edc75f-4844-3495-a93d-7242a51f0555 | -13.95707 | -44.86052 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 88dcf11f-67f2-37ea-bd09-9605a00df5ed | -8.96119 | -45.15239 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 0283f378-ac28-3fc2-9a87-53ad2253824e | -11.6455 | -43.68127 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e40a7cfd-be88-3f78-a79f-b039f208fe76 | -11.78472 | -43.53211 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| d709e133-a9ec-3309-a564-6c608095667b | -9.36271 | -45.95142 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d69afe8f-f9cd-3bc0-afe3-c0907402e04c | -13.43802 | -40.44921 | 2026-10-08 16:18:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.7 |
| 698f0d43-c76e-38fc-8bf9-f6a33c08e3e6 | -11.84407 | -47.35747 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5073abaa-c52e-386a-a5a7-6134780898d6 | -11.64607 | -43.68538 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 82a8f7c8-273f-314c-be0c-e3dff69bf95b | -13.12608 | -46.37038 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2bbc48e1-2b4a-3250-ad0d-5ae8e452d483 | -11.62731 | -43.70379 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 232b401c-65c5-3e60-ae82-263c05644a88 | -11.40697 | -47.57048 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 491679ed-5ef1-3e5b-aadf-f2a76fabeb17 | -11.31049 | -46.69297 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f12df3d1-2f3b-34f9-b3d5-68eefdc62893 | -9.83931 | -46.16655 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce3d75d4-09a2-3c30-8119-5a1c6799efe2 | -11.86106 | -47.36234 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cd893e26-7d3b-3c26-ae4f-4609f4bd1d7a | -10.16447 | -44.67414 | 2026-10-08 16:18:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 10d537d8-4ed9-313f-a658-7f93826e4930 | -9.3436 | -35.66948 | 2026-10-08 16:18:00 | NPP-375 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5aa254d5-7e90-37a2-8f7e-344bb2f084c0 | -10.41975 | -47.27046 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15662920-1021-3eef-bd6d-f2c161c51bd7 | -13.20184 | -47.88423 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3e3efffc-bf0a-37b9-bc43-c33e9c633055 | -10.42017 | -47.27358 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 90e50355-843b-3b96-8cc4-048fc00ffcc2 | -9.9745 | -43.49569 | 2026-10-08 16:18:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6ad2b783-c332-3a91-8f69-01faa521c967 | -13.96459 | -44.84433 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 281fab08-bdf2-3a74-8868-dfdcf3ce8aac | -11.95415 | -47.76461 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83239bf3-e14f-3511-97ed-d67a2fa12bf0 | -8.28522 | -45.73774 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 79012b7c-e660-3a5d-b3f3-7b34abdae200 | -10.52129 | -47.31665 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 720fa47b-2e1e-3de6-b271-3909865a23c1 | -11.1205 | -47.79089 | 2026-10-08 16:18:00 | NPP-375 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 52223f36-25f4-3642-abed-f11401bf72b5 | -8.78249 | -47.26206 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ab6ada8b-f5c5-3ac6-adcd-655fdf5d1962 | -11.20347 | -45.21865 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5a031281-dadb-3505-b279-67f5c4455667 | -9.89278 | -36.48417 | 2026-10-08 16:18:00 | NPP-375 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f69d9358-1e17-3fd5-b913-6a644012f731 | -9.24664 | -45.65361 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1169e128-3dd6-3c51-854d-ea8c5b3605bc | -12.28371 | -38.93962 | 2026-10-08 16:18:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6c07ac7f-4e62-3127-9af8-26a30c938d9f | -8.2904 | -45.74154 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4ec8fa63-4ed3-39f7-a709-e711187c780a | -10.88086 | -47.61079 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94275510-36ca-3f8a-a41d-335048e795e1 | -11.47324 | -43.39674 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ae7b2945-accd-3620-9a7e-c19b037c704e | -11.45488 | -43.38437 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 287b7cb6-2c89-3ba1-b096-dc305718f672 | -10.48081 | -47.25199 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 89afe54f-a4b0-3518-8795-2d13f918f8d7 | -8.84651 | -45.44883 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4acb17dd-04b1-3b00-b23b-e5331709e7ed | -13.19614 | -47.88469 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dfed9ca5-55ea-34b6-9a02-dcef97d781b6 | -10.92828 | -45.39612 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 59f770f2-4fe6-3147-858d-409cdb7d2aab | -8.79837 | -47.04338 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 4dfeeb29-5391-3bd7-b47c-1996f3a04e67 | -12.2485 | -44.75053 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| dff7f766-71ea-3857-8e18-04c3c1c77024 | -11.08109 | -44.01314 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |


[Clique aqui para ver as próximas entradas](README266.md)
