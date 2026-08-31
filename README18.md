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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb66c14a-b76f-30d6-b969-6d4c18f923f1 | -7.97966 | -44.29297 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b45c6d52-939c-380e-88bb-7cfdc61f33ad | -8.38169 | -45.76629 | 2026-08-31 03:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 246fde99-075f-3ab2-a82c-7654057cde9b | -7.1131 | -42.76006 | 2026-08-31 03:53:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30bc55a5-dae6-30ec-9cba-0a731fb6fdc8 | -7.93423 | -44.25018 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5110e4dc-e9b9-3fa0-8297-0b51440864a3 | -6.30532 | -44.6122 | 2026-08-31 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7d59fc5-1d5d-31f9-aff8-13982616716b | -7.62744 | -44.84322 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6f876a8-56bc-3dc7-9c1c-b63b2f1d6c32 | -7.92338 | -44.25139 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8827158-9dad-32d1-ba17-459bc8ae180e | -6.48379 | -43.71078 | 2026-08-31 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ece31e5-26c4-39d3-83d3-99b636e27e9b | -5.60077 | -44.00166 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a9a93d9-7974-35d2-ad49-0c26f702281e | -7.79267 | -43.95679 | 2026-08-31 03:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22034c78-6418-309e-8cdf-7d43f260c154 | -3.41577 | -43.37574 | 2026-08-31 03:53:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d94165a-7d67-3db9-a497-ac6775cc639f | -5.61132 | -44.00332 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94d1a40c-15f8-35ef-b070-148e65511d6c | -8.08421 | -45.47094 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a876882-b651-3048-949e-55d2cfc78a27 | -5.58504 | -42.3279 | 2026-08-31 03:53:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ecca017e-fd7f-3405-963b-6676b4e73c5d | -8.45246 | -46.8953 | 2026-08-31 03:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44b57a79-5047-3756-ae04-e2e3ee75ca99 | -8.38429 | -45.0017 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4f6e0e0-0660-35ca-9f87-50d733e2cb55 | -7.93479 | -44.24704 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 704a79f7-d6e3-3cb3-a0ec-4a51f1fbf8aa | -7.41458 | -44.26267 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4856406-e244-37e8-b032-d44569bd395e | -8.08491 | -45.46707 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 088d5059-27ea-3e9f-a3ca-d4b23bd5b530 | -8.75671 | -45.38057 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f41f3c9a-475d-35c6-83a8-77fbba5f6665 | -8.14327 | -45.5164 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c6fdbf8-145c-3962-9065-a480e978a95f | -7.03838 | -42.19794 | 2026-08-31 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c0bbb06b-95b4-3750-8086-415560671592 | -5.45754 | -42.64447 | 2026-08-31 03:53:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 03a6ddd4-841b-328e-83ea-468c6fe3d297 | -7.9188 | -44.2474 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3399ce6d-fcce-3c54-9cae-1244cc12ce06 | -7.74284 | -44.73823 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66cafc3b-75bf-379e-a24f-1625990abbfc | -6.38157 | -45.46196 | 2026-08-31 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50146ea4-6249-3080-b68e-8e14bddbb07c | -5.6066 | -43.99937 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 42c8ddef-59be-3838-b8c1-02202450e178 | -7.41519 | -44.25926 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26381521-3ac8-3117-8642-7878a4e5b7d9 | -7.97346 | -44.29792 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa578973-4a57-37dc-8036-81cfb9e03ac9 | -8.0834 | -45.47543 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72f8041c-ad3e-366c-88b8-d34479cbe0fa | -9.00466 | -39.88259 | 2026-08-31 03:53:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d1a18f30-6279-3dd5-ba3c-90ca92d10b5d | -7.96294 | -44.32697 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd1dd664-1fc5-3835-9caf-5eee7303a6ec | -8.14257 | -45.52015 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90993606-f9ef-345b-bd66-3a0f883382bd | -7.7932 | -43.95382 | 2026-08-31 03:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 751c08a0-22f4-358b-b2ff-f204efa3efc3 | -5.58974 | -42.32871 | 2026-08-31 03:53:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3cbe0934-6b68-3e67-88da-3536c9873d0b | -7.98132 | -44.28368 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 200e3484-aa43-38f3-a5f5-4580255f3e15 | -7.91825 | -44.2504 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60517c7b-7cf1-3c5b-a779-65e8e6cc72d4 | -7.9802 | -44.28994 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbc5846b-49a0-3e00-a5af-b51216f5bf6c | -5.5906 | -42.32369 | 2026-08-31 03:53:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| efba805e-308e-38f2-8a7e-ecc58fbc3f45 | -8.44659 | -46.89322 | 2026-08-31 03:53:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ea1e9d8f-5eb9-3bb9-98f0-557ef3647d64 | -7.92394 | -44.24836 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6936037-0e4d-33ec-92e1-1226bb278922 | -7.76881 | -44.06061 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61a661c0-c0e4-3b29-a41c-78d710a0b8cc | -7.11221 | -42.76511 | 2026-08-31 03:53:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca4dbac9-9216-36a9-a4c0-f0f26d9effcb | -5.60021 | -44.00483 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5123a4a1-302b-3216-b605-c8c029dcf384 | -5.45095 | -42.65408 | 2026-08-31 03:53:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ce56c3fe-94e5-353c-a4a2-7fe9ca7dbdc6 | -5.60603 | -44.00257 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 59491453-be59-3e2d-bfd2-07360fad6e2c | -7.11869 | -42.7559 | 2026-08-31 03:53:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 38206efb-6c79-3ad1-acfd-a404a64977f8 | -6.38087 | -45.46589 | 2026-08-31 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae63401c-14e0-3278-b3fc-e09451f4660a | -6.91652 | -41.64974 | 2026-08-31 03:53:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 18ed0a08-b3e0-3be2-8030-7095ef8247d8 | -8.38616 | -44.99138 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2722ab18-de05-3927-bf38-2ed16d274e21 | -8.756 | -45.38449 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46461129-fb22-36a8-b341-fd98ce74858b | -8.39155 | -44.9922 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06ca255d-0349-3022-9364-4cdeff47413e | -7.7375 | -44.73732 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6eb9f6be-c355-30bf-a936-c847c82137c3 | -6.18536 | -44.93687 | 2026-08-31 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3c2c0cc-e796-3d0e-90cb-6faaec2de981 | -7.20852 | -42.74129 | 2026-08-31 03:53:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 55545d7c-5877-33eb-999c-8330dd16de6c | -8.72807 | -45.38272 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bcd42da6-b7ad-3ef9-9c08-12cff0cb5d2e | -7.97556 | -44.28616 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5898a52-64a6-3ec9-a392-0c82e6c0abe1 | -7.60866 | -44.88527 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d4836e9-3d2e-3ba9-ada6-9d9070655da5 | -6.38302 | -45.46107 | 2026-08-31 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99b8dda7-e1cb-337b-8e57-a7fa4ca00913 | -5.1911 | -35.84872 | 2026-08-31 03:53:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d2703cd0-7540-344f-b756-15ba268a2067 | -7.10748 | -42.76434 | 2026-08-31 03:53:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ceadf654-24c1-3152-bb95-0dd90ba4247f | -7.63284 | -44.84405 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec9869b3-d03c-3661-a107-c33d49f00430 | -6.48682 | -43.71089 | 2026-08-31 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f99cf595-ea08-3a0c-8742-bc793c45c0dd | -7.92851 | -44.2524 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7054f14a-14ce-340d-96a7-5fa89e1cbd07 | -7.54871 | -47.32605 | 2026-08-31 03:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbd38ee0-b72b-35fe-8aa0-e7522ad2f989 | -7.76824 | -44.06378 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 468bf1a5-7ff9-3d00-b5e9-5056f5a57434 | -7.60803 | -44.88873 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b1aafc7-aa46-3a28-a8da-9956181a9151 | -7.61407 | -44.88614 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c25de610-4912-3a32-8b89-bb752ed18eeb | -7.9177 | -44.25342 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae14e942-1328-3003-bc5c-2bc549085e5f | -6.86847 | -44.43403 | 2026-08-31 03:53:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 046786c0-882e-3304-8345-87c8b5f206ac | -8.37832 | -45.00404 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4451e3f3-8a61-39dd-9d4b-dfff7d80fb5d | -8.74478 | -46.44782 | 2026-08-31 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39929a41-e083-3e73-93da-169ad8244ae3 | -6.48627 | -43.71394 | 2026-08-31 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 633f486d-4cc7-35e9-a205-5f96cf37a666 | -7.97671 | -44.27973 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68fcd1e9-0307-311a-a0b5-14c1c34a4c95 | -6.17982 | -44.93589 | 2026-08-31 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08adc33f-cfe2-3db1-afb7-e4915808ea1d | -8.15124 | -45.4733 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c9391aa9-cefe-3df4-9caa-cce4f36853af | -5.60547 | -44.00578 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89bccc30-c35a-3965-8edb-a972c19be6be | -8.1047 | -45.47641 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03a56712-ae33-3995-804d-af1590d13f61 | -7.78805 | -43.95345 | 2026-08-31 03:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8f0b1e1-ca18-3f85-89c8-f483fcc9f926 | -7.97295 | -44.30077 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b47fa5f9-1552-34e9-9164-a022d7f737ad | -8.0785 | -45.47075 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8398ec23-2739-3428-a571-f1a5067e82a2 | -6.48884 | -43.71189 | 2026-08-31 03:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfc31734-03a0-32a9-944a-ea14b380c8cc | -5.19501 | -35.84574 | 2026-08-31 03:53:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c093fd2c-c5c3-34c3-a696-6c6ff0504b33 | -8.0792 | -45.46693 | 2026-08-31 03:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68737676-b654-3be6-8b0d-8554f2218f92 | -6.87487 | -41.65556 | 2026-08-31 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2ed09b7-a110-344e-ad3a-289f1cf20c7a | -8.72878 | -45.37883 | 2026-08-31 03:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 14e5f231-f565-30e8-bd18-06c15d801029 | -7.93366 | -44.2533 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fcfcdde-d702-357c-ad99-cc4d8f8481da | -6.30471 | -44.61565 | 2026-08-31 03:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f105858-3495-3237-9269-11d5640d44f8 | -3.41525 | -43.37892 | 2026-08-31 03:53:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be52a1f9-d807-3003-a4d5-d0d1e4b92e8f | -7.92283 | -44.25441 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5ea30d3-889f-3294-ac70-9d0213e8b87d | -7.4112 | -44.25163 | 2026-08-31 03:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b21a4188-1216-3bc9-a862-5ef4e583a1d7 | -7.97613 | -44.28295 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d683b956-9da7-366f-8977-feac1ad84459 | -5.61076 | -44.00652 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 064e793e-7cc7-3887-b82a-502bfba6a080 | -7.97913 | -44.29596 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72c94eb5-c12a-39f5-94fc-d0d55a519d9f | -7.04446 | -42.18979 | 2026-08-31 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6f6bb1a6-b38d-3931-80e0-718ddaae0c65 | -8.75068 | -46.44867 | 2026-08-31 03:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f4da269-60ea-3fb8-9cd2-e080e16eb760 | -6.38228 | -45.46506 | 2026-08-31 03:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adc174a8-942b-3e45-8d2b-e6d592930753 | -7.96239 | -44.33007 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 592bf4f1-4796-340e-9829-0c7fa876cff5 | -7.91661 | -44.25941 | 2026-08-31 03:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f664c56a-7b81-34ad-89cc-57316968f0a0 | -5.60134 | -43.99848 | 2026-08-31 03:53:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README19.md)
